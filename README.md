# SteamLinuxChecker
Ever wondered if you're a true Linux gamer?

# HowTo
```sh
$ sudo apt-get install python3.5
$ git clone --recursive https://github.com/cprn/steamlinuxchecker.git
$ cd steamlinuxchecker
$ cp config_example.ini config.ini
$ vim config.ini # set your Steamp API key in here
$ ./checkuser {vanity_name|profile_id}
$ ./checkgroup {group_name}
```

# Vanity and Group
* http://steamcommunity.com/id/cprn
* http://steamcommunity.com/profiles/76561198090757837
* http://steamcommunity.com/groups/LinuxUsersExclusively

Both `cprn` and `76561198090757837` will work for `checkuser`.
The name of the group `LinuxUsersExclusively` will work for `checkgroup`.

# Notes
SteamAPI currently doesn't provide available platforms, hence, www scraping.
Data is stored in simple file based cache in `~/tmp/steamwww_cache.pkl`.
First run will be slow, next runs will have most of the platform info cached.
