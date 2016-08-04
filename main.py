#!/usr/bin/python3
import configparser
import os
import steamapi.steamapi as steamapi

config = configparser.ConfigParser()
config.read('config.ini')

try:
    steamapi.core.APIConnection(api_key=config['api']['key'])
except KeyError:
    raise SystemExit('Copy config_example.ini to config.ini and set the api.key value!')

user = steamapi.user.SteamUser(userurl="cprn")

total = 0
for game in user.games:
    total += game.playtime_forever
    print(game.id, game.name, game.playtime_forever)
    print(dir(game.from_api_response))
    raise SystemExit

print("\nTotal playtime: %s" % total)

#  '_cache', '_id', '_owner', '_schema', '_userid', 'achievements', 'appid', 'from_api_response', 'id', 'name', 'owner', 'playtime_forever'
