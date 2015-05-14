OFFYT
=====
#####Offline YouTube Playlist Synchronization

This is a really small project that enables you to keep an YouTube playlist
synchronized on your computer. The idea is that you run this script in a cronjob
that will check, every 5 minutes or so, if it needs to download or remove videos
from that playlist.


Installation
------------

```bash
git clone git@github.com:koenbollen/offyt.git
cd offyt
pip install -r requirements.txt
python offyt.py --help
```

SetupTools coming soon...


Usage
-----

```bash
offyt [-v] PLAYLIST [OUTPUTDIR]
```

Where -v is verbose and OUTPUTDIR defaults to the current working directory.
