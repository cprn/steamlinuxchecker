# SteamLinuxChecker
Ever wondered if you're a true Linux gamer?

# HowTo
Requires `python3.5` or newer and a [Steam API key](https://steamcommunity.com/dev/apikey).

Example installation instructions on Debian-like systems:

```sh
$ sudo apt-get install python3.5
$ git clone --recursive --depth 1 https://github.com/cprn/steamlinuxchecker.git
$ cd steamlinuxchecker
$ cp config_example.ini config.ini
$ vim config.ini # set your Steamp API key in here
$ ./checkuser {vanity_name|profile_id}
$ ./checkgroup {group_name}
```

# Vanity and Group
* https://steamcommunity.com/id/cprn
* https://steamcommunity.com/profiles/76561198090757837
* https://steamcommunity.com/groups/LinuxUsersExclusively

Both `cprn` and `76561198090757837` will work for `checkuser`.
The name of the group `LinuxUsersExclusively` will work for `checkgroup`.

# Notes
Platform data is stored in simple file based cache in `~/tmp/steamwww_cache.pkl`.
First run will be slow, next runs will have most of the platform info cached.
Cached data older than 90 days is refreshed to handle adding or dropping Linux support.
