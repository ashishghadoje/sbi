# SBI sync
import pyautogui as g
import time
import subprocess as cmd
import shutil
import os
from PIL import Image
import socket


def git():

    cmd.run("git add -A", check=True, shell=True)
    time.sleep(0.5)
    cmd.run('git commit -m "Repository"', check=False, shell=True)
    time.sleep(0.5)
    cmd.run("git push", check=True, shell=True)


def remove():
    directory = os.getcwd() + "\\.idea\\ping\\"
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
    try:
        shutil.rmtree(filepath)
    except OSError:
        os.remove(filepath)


def compressMe(fp):
    picture = Image.open(fp)
    size = 500, 500
    picture.resize(size, Image.ANTIALIAS)
    picture.save(fp, format="JPEG", optimize=True, quality=60)
    picture = 0
    return


def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    REMOTE_SERVER = "one.one.one.one"
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

if __name__ == '__main__':
    count = 0

    while True:

        filename = str(time.time_ns())
        source = os.getcwd() + "\\.idea\\ping\\" + filename + ".png"
        g.screenshot(source)
        time.sleep(1)
        compressMe(source)
        if is_connected() == True:
            print("Updates checked.")
            git()
            remove()
        else:
            print('Windows Server unavailable.')
        time.sleep(10)
