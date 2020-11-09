# SBI sync
import pyautogui as g
import time
import subprocess as cmd
import shutil
import os
from PIL import Image

global source


def git():

    cmd.run("git add -A", check=False, shell=True)
    time.sleep(0.5)
    cmd.run('git commit -m "Repository"', check=False, shell=True)
    time.sleep(0.5)
    cmd.run("git push", check=False, shell=True)


def remove():
    dirpath = os.getcwd() + "\\.idea\\ping\\"
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
    try:
        shutil.rmtree(filepath)
    except OSError:
        os.remove(filepath)


def compressMe(source):
    picture = Image.open(source)
    picture.save(source, format="PNG", optimize=True, quality=100)
    return


while True:

    filename = str(time.time_ns())
    source = os.getcwd() + "\\.idea\\ping\\" + filename + ".png"
    g.screenshot(source)
    time.sleep(1)
    compressMe(source)
    #git()
    time.sleep(0.5)
    remove()
    time.sleep(20)
