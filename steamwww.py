#!/usr/bin/python3
import requests
import sys
import time
from simplecache.cache import PickleCache

class Scraper:

    def __init__(self):
        self.__cache = PickleCache("~/tmp/steamwww_cache.pkl", 86400 * 21)
        self.__calls = 0

    def get_html(self, id):
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

    # TODO: use DOM to read app platforms and ignore bundles
    def runs_on_linux(self, id):
        try:
            linux = self.__cache.get(id)['linux']
            print ('   ', end = '')
        except KeyError:
            linux = self.get_html(id).find("platform_img linux") > 0
            self.__cache.add(id, {"linux": linux})
            self.__cache.save()
            print(' + ', end = '')
        return linux


if __name__ == "__main__":
    print(Scraper().runs_on_linux(sys.argv[1]))
