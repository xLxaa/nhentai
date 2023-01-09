#!/usr/bin/env python3

"""
A simple Python script for downloading a doujin from nhentai.net.

The idea behind this script is to allow for much easier downloads of doujins
with the current Cloudfare protection being enabled on the main site. To try
and bypass issues with the API that nhentai used to provide, this script is in
fact rather primitive and also targets the doujin image directory site
<https://i3.nhentai.net/galleries/> (can be i7/ i5 I just chose randomly).
"""

from urllib.parse import urljoin
from os import path, mkdir
from argparse import ArgumentParser

from requests import Session


def main():
  _BASE_URL = "https://i3.nhentai.net/"
  _DEST = "/galleries/"
  _FULL_BASE_URL = urljoin(_BASE_URL, _DEST)

  session = Session()  # Persistent session using `requests.Session()`.

  ask_for_media_id = int(input("First enter the doujin's media ID: "))
  ask_for_how_many_pages = int(input("Second, how many pages to download? "))

  # Create directory if it does not exist `./<media_id>/`.
  if path.exists(str(ask_for_media_id)) is False: mkdir(str(ask_for_media_id))

  for page in range(ask_for_how_many_pages):
    """
    This try except is lazy, it will silence errors entirely, however it was
    an easy solution to find out the image extension for the current page.
    I don't think it is the best solution as it does not account for very many
    extension types and again silences errors.
    """
    try:  # Try with .jpg in dest URL, if resp 404 then trigger except block.
      jpg_url = urljoin(_FULL_BASE_URL, f"{ask_for_media_id}/{page + 1}.jpg")
      resp_obj = session.get(jpg_url)
      img_ext = ".jpg"
      if resp_obj.ok is False: raise IndexError
    except:  # Exception triggered, type set to .png for URL and file.
      png_url = urljoin(_FULL_BASE_URL, f"{ask_for_media_id}/{page + 1}.png")
      resp_obj = session.get(png_url)
      img_ext = ".png"
      if resp_obj.ok is False: break  # Not a valid page num/ png. We're done.

    # Write the page's bytes into image file which depends on above try/ excp.
    with open(f"{ask_for_media_id}/{page + 1}{img_ext}", "wb") as file_obj:
      file_obj.write(resp_obj.content)

  print("\nAll done! Check the newly created directory.")


if __name__ == "__main__":
  description = "Enter the media ID (not the normal ID) of a doujin and the "\
          "number of pages you want to download, the script does the rest "  \
          "for you. To get a doujin's media ID on nhentai.net, you can open "\
          "the cover image location (right click > open image in new tab) "  \
          "and then find it in the destination URL: "                        \
          "https://i3.nhentai.net/galleries/<media_id>/1.png"
  parser = ArgumentParser(prog="Nhentai Scuffed Script",
                          description=description,
                          usage="main.py <option>")
  args = parser.parse_args()

  print("-----| Nhentai Scuffed Script |-----\n")
  print("Try `-h/--help` to see example usage.\n")

  main()
