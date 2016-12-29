#!/usr/bin/python3
import requests
import sys
import time
from simplecache.cache import PickleCache

class Scraper:

    def __init__(self):
        self.__cache = PickleCache("~/tmp/steamwww_cache.pkl", 86400 * 90)
        self.__calls = 0

    def get_html(self, id): # TODO: retire
        self.__calls += 1
        self.__calls % 20 == 0 and time.sleep(2) # sometimes wait between calls
        r = requests.get('http://store.steampowered.com/app/%s' % id, cookies={
            'birthtime': '1000',
            'path': '/',
            'domain': 'store.steampowered.com'
            })
        assert r.status_code == 200, "Can't open %s (%d)" % (id, r.status_code)
        assert r.text.find('enter your birth') < 0, "Age check error! %d" % id
        return r.text

    def get_json(self, id): # TODO: can take multiple comma separated ids
        time.sleep(1) # sleep between each call
        r = requests.get('http://store.steampowered.com/api/appdetails/?appids=%s' % id)
        j = r.json()[str(id)]
        assert r.status_code == 200, "Can't open %s (%d): %s" % (id, r.status_code, r.json())
        return j

    def runs_on_linux(self, id, verbose = False):
        try:
            linux = self.__cache.get(id)['linux']
            verbose and print('   ', end = '')
        except KeyError:
            try:
                j = self.get_json(id)
                linux = j['data']['platforms']['linux'] if j['data']['type'] == 'game' else True
            except KeyError:
                linux = False
            self.__cache.add(id, {"linux": linux})
            self.__cache.save()
            verbose and print(' + ', end = '')
        return linux


if __name__ == "__main__":
    print(Scraper().runs_on_linux(sys.argv[1]))
