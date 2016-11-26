import swhlog
from swhlog import log,attention

# it's easy to log things with log()
log("any message you want")

# optionally a loglevel can be defined
log("this is an important message",1)

# if loglevel>3, it will be logged but not displayed
log("this is not important",5)

# attention() sends a message to console without logging it
attention("turning debug mode on")
swhlog.debugMode=True # causes more informationt to display
log("debug mode shows details!")

# now launch the output in the web browser
swhlog.getLogHTML()