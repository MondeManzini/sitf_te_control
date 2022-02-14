# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:23:49 2020

@author: Rishad modifed by Sias 
@modify: Monde: 14-02-2022
        : 
"""

import socket

PORT = 22
HOST = '10.8.88.166'

def initSigGen(HOST,PORT):
    """
    Identify instrument. Can be used as a connectivity check
    """
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b'*IDN?\r\n')
    data=s.recv(1024)
    print('Received', data)
    state=0
    setstate='OUTP1 {}\r\n'.format(state)
    s.sendall(bytes(setstate))
    s.sendall(b'OUTP1?\r\n')
    data=s.recv(1024)
    s.close()
    if data.decode('UTF-8')=='1\n':
        print("RF Output On")
    else: print("RF Output Off")

def setSigGenPower(HOST, PORT, power):
    """
    Identify instrument. Can be used as a connectivity check.
    """
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    setpower = 'POW {}\r\n'.format(power)
    s.sendall(bytes(setpower))
    s.sendall(b'POW?\r\n')
    data = float(s.recv(1024))
    print("Sig gen power = %f dBm" %data)

def setSigGenFreq(HOST, PORT, Freq):
    """
    Identify instrument. Can be used as a connectivity check.
    """
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    setfreq= "FREQ {}\r\n".format(Freq)
    s.sendall(bytes(setfreq))
    s.sendall(b'FREQ?\r\n')
    data = float(s.recv(1024))
    s.close()
    print("Sig gen frequency = % MHz" %(data/1e6))

def setSigGenState(HOST, PORT,state):
    """
    Identify instrument. Can be used as a connectivity check.
    """
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    setstate='OUTP1 {}\r\n'
    s.sendall(bytes(setstate))
    s.sendall(b'OUTP1?\r\n')
    data=s.recv(1024)
    s.close()
    if data.decode("UTF-8") == "1\n":
        print("RF Output")
    else: print(("RF Output OFF"))

