import sys
import configparser
from steamapi import steamapi
from steamwww import Scraper


def get_steam_api():
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        steamapi.core.APIConnection(api_key=config['api']['key'])
    except KeyError:
        raise SystemExit('Copy config_example.ini to config.ini and set the api.key value!')
    return steamapi

def get_steam_user(steamapi, id):
    try:
        try:
          user = steamapi.user.SteamUser(userid=int(id))
        except ValueError:
          user = steamapi.user.SteamUser(userurl=id)
    except steamapi.errors.UserNotFoundError:
        raise SystemExit('User not found.')
    return user

def check_steam_user(user, verbose = False):
    total = 0
    linux = 0
    scraper = Scraper()
    try:
        for game in user.games:
            total += game.playtime_forever
            badge = '-----'
            if scraper.runs_on_linux(game.id, verbose):
                badge = 'LINUX'
                linux += game.playtime_forever
            verbose and sys.stdout.write(badge + ' %6s ' % game.playtime_forever + game.name + "\n")
            verbose and sys.stdout.flush()
    except steamapi.errors.AccessException:
        verbose and sys.stdout.write('(private)')
        verbose and sys.stdout.flush()
        pass

    score = 0
    if total > 0:
        score = linux/total

    summary = "\nTotal playtime: {}\nLinux playtime: {}\nPlaytime score: {:0%}\n"
    stats = (total, linux, score)
    verbose and sys.stdout.write(summary.format(*stats))
    return stats

