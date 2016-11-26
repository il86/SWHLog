html="""<html>
<head>
<style>
body{font-family: monospace, courier, sans-serif;}
.loglevel {padding: 2px;}
.loglevel0 {background-color: #FFAAAA;}
.loglevel1 {background-color: #FFCCCC;}
.loglevel2 {background-color: #CCFFCC;}
.loglevel3 {background-color: #CCCCFF;}
.loglevel4 {}
.loglevel5 {color: rgba(0,0,0,.5)}
.loglevel6 {color: rgba(0,0,0,.4)}
.loglevel7 {color: rgba(0,0,0,.3)}
.loglevel8 {color: rgba(0,0,0,.3)}
.loglevel9 {color: rgba(0,0,0,.3)}

.timer {font-size: x-small; padding-right: 20px; color: rgba(0,0,0,.5)}
</style>
</head>
<body>
CONTENT
</body>
</html>"""

def htmlsafe(msg):
    """convert characters to html that would otherwise break it."""
    msg=msg.replace("<","&lt;").replace(">","&gt;")
    msg=msg.replace("\n","<br>")
    return msg