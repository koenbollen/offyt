OFFYT
=====
#####Offline YouTube Playlist Synchronization

This is a really small project that enables you to keep an YouTube playlist
synchronized on your computer. The idea is that you run this script in a cronjob
that will check, every 5 minutes or so, if it needs to download or remove videos
from that playlist.

My setup: I have an playlist called "Offline Android", keep that synchronized to
my server and keep _that_ synchronized to my phone when on WiFi.


Installation
------------

```bash
git clone git@github.com:koenbollen/offyt.git
cd offyt
python setup.py build
sudo python setup.py install
```


Usage
-----

```bash
offyt [-v] PLAYLIST [OUTPUTDIR]
```

Where -v is verbose and OUTPUTDIR defaults to the current working directory.
