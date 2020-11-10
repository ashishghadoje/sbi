# SBI sync
import pyautogui as g
import time
import subprocess as cmd
import shutil
import os
from PIL import Image


def git():

    cmd.run("git add -A", check=True, shell=True)
    time.sleep(0.5)
    cmd.run('git commit -m "Repository"', check=False, shell=True)
    time.sleep(0.5)
    cmd.run("git push", check=True, shell=True)


def remove():
    dirpath = os.getcwd() + "\\.idea\\ping\\"
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
    try:
        shutil.rmtree(filepath)
    except OSError:
        os.remove(filepath)


def compressMe(fp):
    picture = Image.open(fp)
    size = 1000, 1000
    picture.resize(size, Image.ANTIALIAS)
    picture.save(fp, format="PNG", optimize=True, quality=100)
    return


if __name__ == '__main__':

    while True:

        filename = str(time.time_ns())
        source = os.getcwd() + "\\.idea\\ping\\" + filename + ".png"
        g.screenshot(source)
        time.sleep(1)
        compressMe(source)
        #git()
        time.sleep(0.5)
        #remove()
        time.sleep(20)
