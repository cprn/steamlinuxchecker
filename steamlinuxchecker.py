import sys
import configparser
from steamapi import steamapi
from steamwww import Scraper


scraper = Scraper()


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
        user.name += ' (private)'
        pass

    score = 0
    if total > 1:
        score = linux/total

    stats = (total, linux, score)
    verbose and print_user_summary(user, stats)
    return stats

def print_user_summary(user, stats):
    sys.stdout.write("\nSteamID: {}\nUser: {}\nProfile: {}\nTotal: {:5d}h {:2d}m\nLinux: {:5d}h {:2d}m\nScore: {:10.2%}\n".format(
        user.id,
        user.name,
        user.profile_url,
        *divmod(stats[0], 60),
        *divmod(stats[1], 60),
        stats[2]
    ))
    sys.stdout.flush()

