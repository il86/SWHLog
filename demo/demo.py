import sys
sys.path.insert(0,'../')

import swhlog
from swhlog import log,attention

def logTest1():
    """simplest example."""
    attention("very simple usage") # displayed in console, not saved
    log("This is easier than I thought!") # displayed and logged.

def logTest2():
    """more advanced usage."""
    attention("more advanced usage")
    
    log("Level 0: system critical error causing immediate exit",0)
    log("Level 1: important message the user NEEDS to know",1)
    log("Level 2: primary code blocks",2)
    log("Level 3: common actions",3)
    log("Level 4: useful debug unformation",4)
    log("Level 5: super extra information",5)

def logTest3():
    """every log level."""    
    attention("displaying every log level")
    # show how loglevel messages are suppressed above "logLevel"
    for i in range(10):
        log("loglevel %d"%i,i)
    
    # show the details we get when debugMode is enabled
    swhlog.debugMode=True
    for i in range(10):
        log("loglevel %d"%i,i)
        
if __name__=="__main__":
    
    logTest1() # log some stuff
    swhlog.getLogHTML(title="SWHLog Simple Demo") # show the result
    swhlog.clear() # start over by erasing the log
    
    logTest3() # log some stuff
    swhlog.getLogHTML(title="SWHLog Every Log Level") # show the result
    swhlog.clear() # start over by erasing the log
    
    logTest2() # log some stuff
    swhlog.getLogHTML(title="SWHLog Advanced Demo") # show the result
    swhlog.clear() # start over by erasing the log