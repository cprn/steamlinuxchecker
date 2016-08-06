# SteamLinuxChecker
Ever wondered if you're a true Linux gamer?

# HowTo
```sh
$ sudo apt-get install python3
$ git clone --recursive https://github.com/cprn/steamlinuxchecker.git
$ cd steamlinuxchecker
$ cp config_example.ini config.ini
$ vim config.ini # set api.key
$ ./steamlinuxchecker {vanity_name|profile_id}
```

# Vanity
* http://steamcommunity.com/id/cprn
* http://steamcommunity.com/profiles/76561198090757837

Both `cprn` and `76561198090757837` will work.

# Notes
SteamAPI currently doesn't provide available platforms, hence, www scraping.
Data is stored in simple file based cache in `~/tmp/steamwww_cache.pkl`.
First run will be slow, next runs will have most of the platform info cached.
