import os
import subprocess

def pingDns():

    with open(os.devnull, "wb") as consoleOut:    
        output = subprocess.Popen(['ping', '-c', '1', '-W', '2', '8.8.8.8'],
            stdout=consoleOut, stderr=consoleOut).wait()

        if output:
            print ("Host is down")

        else:
            print ("Host is up")
            consoleOut.read
