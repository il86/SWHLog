import time
import inspect
import os
import tempfile
import webbrowser
import swhlog.htmltemplate

swhlog.logLevel=5 # hide messages higher than this number
swhlog.debugMode=False

# [fileName,lineNumber,funcName,timeAbs,timeDiff,level,message]
# [0       ,1         ,2       ,3      ,4       ,5    ,6      ]
loglines=[] 

def clear():
    """erases the entire log."""
    global loglines
    loglines=[]
    return

def attention(msg=""):
    """attention - show an important message with no frills."""
    print("\n"+"#"*50+"\n"+"#"*3,msg.upper()+"\n"+"#"*50+"\n")
    return

def log(message="",level=3):
    """log (show/save) a message."""
    message=message.strip()
    timeAbs=time.clock()
    line="[%s] %s %s"%("%.04f"%timeAbs,"-"*level,message)
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    fileName,lineNumber,funcName=calframe[1][1:4]
    fileName=os.path.basename(fileName)
    if len(loglines):
        timeDiff=timeAbs-loglines[-1][3]
    else:
        timeDiff=timeAbs
    logline=[fileName,lineNumber,funcName,timeAbs,timeDiff,level,message]
    loglines.append(logline)    
    if swhlog.debugMode:
        line="%s:%d:%s() "%(fileName,lineNumber,funcName)+line
    if level<=swhlog.logLevel:
        print(line)
    return

def getLogText():
    """returns saved log as a string."""
    text=[]
    for line in loglines:
        fileName,lineNumber,funcName,timeAbs,timeDiff,level,message=line
        t="%d %s:%d:%s() "%(level,fileName,lineNumber,funcName)
        t+="[%s] %s"%("%.04f"%timeAbs,message)
        text.append(t)
    return "\n".join(text)
    
def getLogHTML(saveAs=False,launch=True,title="SWHLog Report"):
    """
    generate pretty HTML page from saved log.
    
    If saveAs is given a path name, it wil save the HTML document as that file.
    Otherwise, it will create a file in the temporary folder.
    
    If launch is True, it will open the file in a browser after saving it.
    """
    html="<h1>%s</h1>"%title
    for line in loglines:
        fileName,lineNumber,funcName,timeAbs,timeDiff,level,message=line
        message=swhlog.htmltemplate.htmlsafe(message)
        message2="&nbsp;"*level*3+message
        message2='<span class="timer">%s</span> '%("%.04f"%timeAbs)+message2
        html+='<div class="loglevel loglevel%d">%s</div>'%(level,message2)
    html+="<hr><h1>Text Log</h1>"
    html+='<code>%s</code>'%(swhlog.htmltemplate.htmlsafe(getLogText()))
    fname=os.path.abspath(tempfile.gettempdir()+"/swhlog_%f.html"%time.time())
    with open(fname,'w') as f:
        f.write(swhlog.htmltemplate.html.replace("CONTENT",html))
    print("SAVED:",fname)
    webbrowser.open_new_tab(fname)
    return

if __name__=="__main__":
    print("DONT RUN THIS DIRECTLY.")
    #logTest()
    #getLogHTML()
