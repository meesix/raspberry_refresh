#!/usr/bin/python3
from urllib.request import urlopen
import time
import subprocess

token = ''

while True:
    with urlopen("https://warehouse.izolyatsia.org/pi.txt") as conn:
        resp = conn.read()
        if resp != token:
            token = resp
            process = subprocess.Popen(['bash', '/home/pi/refresh.sh'], stdout=subprocess.PIPE)
            output, error = process.communicate()
            print("REFRESH %s" % output)
        time.sleep(2)
