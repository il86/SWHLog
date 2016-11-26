"""
The author is intended to run this..
"""
import sys
import os
import shutil
import glob
import subprocess
import webbrowser
import time

def newVersion():
    """increments version counter in version.py"""
    version=None
    fname='../swhlog/version.py'
    with open(fname) as f:
        raw=f.read().split("\n")
        for i,line in enumerate(raw):
            if line.startswith("__counter__"):
                if version is None:
                    version = int(line.split("=")[1])
                raw[i]="__counter__=%d"%(version+1)
    with open(fname,'w') as f:
        f.write("\n".join(raw))
    print("upgraded from version %03d to %03d"%(version,version+1))

def cleanUp():
    for delThis in ['../swhlog.egg-info/']:
        if os.path.exists(delThis):
            shutil.rmtree(delThis)
    for fname in glob.glob("../dist/*.zip"):
        os.remove(fname)
    for fname in glob.glob("../dist/*.tar.gz"):
        os.remove(fname)

def upload():    
    print("packaging and uploading...")
    cmd="cd ../ && python setup.py sdist upload" # -- quiet ?
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line.decode('utf-8').strip())
    retval = p.wait()
    if retval:
        print("process returned value:",retval)
        input("press ENTER to exit...")
    else:
        print("success!")

        
if __name__=="__main__":
    dotsPerSec=2
    secPause=5
    newVersion()
    cleanUp()
    print("\n\nnew version created, preparing to upload ",end='')
    for i in range(secPause*dotsPerSec):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1/dotsPerSec)
    print()
    upload()
    cleanUp()
    webbrowser.open_new_tab('http://pypi.python.org/pypi/swhlog')
    print("PyPi upload successful!")
    print("\n\npreparing to perform local upgrade ",end='')
    for i in range(secPause*dotsPerSec):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1/dotsPerSec)
    print()
    os.system('pip install --upgrade --no-cache-dir swhlog')
    print("\n ~ new version was published and installed ~\n")
        
