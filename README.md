# Nhentai Scuffed Script

A simple script to avoid Cloudflare bs on nhentai.net. This script is the best
I was able to do, it's a bit hard to make it user friendly now that the public
API on nhentai.net is very difficult to use due to Cloudflare being enabled.


## Setup

(Written and tested using Python 3.11.0, should be fine on Windows & Linux)

Install the requirements (requests) with pip:

```bash
python3 -m venv venv && source ./venv/bin/activate  # Optional less clutter.

pip install -r requirements.txt
```


## Usage

You just need to run `main.py` once the requirements are installed.

Once you have ran the script, you just need to enter the doujin's media ID
(not it's normal ID) which can be found by opening one of the doujin's pages
location in another tab or by copying it's address directly, for example
lets just use the cover image, you can get it's location by doing the
following `right click > open image in new tab` (in most browsers) then you
can find the media ID inside of the destination URL in the address bar:
`https://i3.nhentai.net/galleries/<media_id>/1.png`.
