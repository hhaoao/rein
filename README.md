# rein
Software package download tool

# System requirements

only windows 7 or later.

# dependence

*. (aria2)[https://aria2.github.io]: Must be turned on JSON RPC.

*. (git)[https://gitforwindows.org]: Used for update.

*. (scoop's buckects)[https://github.com/lukesampson/scoop/blob/master/buckets.json]:

download Main bucket.

>cd C:\Users\Administrator\Documents\
>mkdir buckets && cd buckets
>git clone https://github.com/ScoopInstaller/Main.git

rein.ini

`buckets = C:\Users\Administrator\Documents\buckets`


## guide
1. aria2 config.
  The configured files are in `aria2config`.

1. Modify path, proxy, etc in `*.conf` .

1. Modify `rein.ini`.

1. rein.exe: Command line tool. see more `--help`

  > rein.exe --download 7zip aria2

1. rein.ini: Configuration file.


