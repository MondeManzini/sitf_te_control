# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:23:49 2020

@author: Rishad modifed by Sias 
@modify: Monde: 14-02-2022
        : Added the host and port numbers
        : Copied Power and Frequency from the NoiseIncreaseRev1.py
          for sig gen use only
Mod Gen ?
Modulation ?
"""

import socket
import time
# The script uses raw ethernet socket communication, and thus VISA library/installation is not required

# -----------Connection Settings--------------
PORT = 5025             # default SMB R&S port 
HOST = '10.8.88.166'    # 
#---------------------------------------------

# -----------Source Settings------------------
Power = -25
Freq = 1500e6
# --------------------------------------------

#-------------Modulation Settings-------------
OFF = 'OFF'
ON = 'ON'
AM_Mod = 'AM'
FM_Mod = 'FM'
PM_Mod = 'PM'
# --------------------------------------------

def initSigGen(HOST,PORT):
    """
    Identify instrument. Can be used as a connectivity check
    """
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if s:
        print("Connection succesful.")
    s.connect((HOST, PORT))
    s.settimeout(1)
    s.sendall(b'*IDN?\r\n')                             
    data = s.recv(1024)
    print('Received', data)
    sig_gen_id = data               # for testing
    state=0
    setstate='OUTP1 {}\r\n'.format(state)
    s.sendall(bytes(setstate, encoding='utf8'))
    s.sendall(b'OUTP1?\r\n')
    data=s.recv(1024)
    set_state = data                # for testing
    print('Received', data)
    s.close()
    if data.decode('utf8')=='1\n':      # 
        print("RF Output On")
    else: print("RF Output Off")

def setSigGenPower(HOST, PORT, power):
    """
    Identify instrument. Can be used as a connectivity check.
    """
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    setpower = 'POW {}\r\n'.format(power)
    s.sendall(bytes(setpower, encoding='utf8'))
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
    s.sendall(bytes(setfreq, encoding='utf8'))
    s.sendall(b'FREQ?\r\n')
    data = float(s.recv(1024))
    s.close()
    print(f"Sig gen frequency = {(data/1e6)} MHz")

def setSigGenState(HOST,PORT,state):
    """
    Identify instrument. Can be used as a connectivity check.
    """
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    setstate='OUTP1 {}\r\n'.format(state)
    s.sendall(bytes(setstate, encoding='utf8'))
    s.sendall(b'OUTP1?\r\n')
    data=s.recv(1024)
    print('Received', data)
    s.close()
    if data.decode("UTF-8") == "1\n":
        print("RF Output On")
    else: print(("RF Output Off"))

def setSigGenModsState(HOST, PORT,ModsState):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    setModsState='MOD:STAT {}\r\n'.format(ModsState)
    s.sendall(bytes(setModsState, encoding='utf8'))
    s.sendall(b'MOD:STAT?\n')
    data=s.recv(1024)
    print('Received', data)
    s.close()
    if data.decode("UTF-8") == "0\n":
        print("All modulations Off")
    else: print(("All modulations On"))


def setSigGenModltn(HOST,PORT,Modltn):
    """
    This function sets on different modulations:
    Usage:
        AM: string
        PM: string
        FM: string
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST, PORT))
    except Exception as e:
        print(e,"Check to see if the port number is {PORT}")
    setstate='{}:STAT ON\r\n'.format(Modltn)
    s.sendall(bytes(setstate, encoding='utf8'))
    s.sendall(b'{Modltn}:STAT?\r\n')
    data=s.recv(1024)
    print('Received', data)
    s.close()
    if data.decode("UTF-8") == "1\n":
        print("{Modltn} Modulation On")
    else: print("{Modltn} Modulation On")

def setupSigGen():
    initSigGen(HOST,PORT)
    time.sleep(2)                       # Wait a bit
    setSigGenPower(HOST,PORT,Power)
    time.sleep(2)                       # Wait a bit
    setSigGenFreq(HOST,PORT,Freq)
    time.sleep(2)                       # Wait a bit
    setSigGenState(HOST,PORT,1)         # Turn on sig gen output
    time.sleep(2)                       # Wait a bit
    setSigGenModsState(HOST,PORT, OFF)  # Switch all modulations off
    time.sleep(2)                       # Wait a bit
    setSigGenModsState(HOST,PORT, ON)   # Switch all modulations off
    time.sleep(2)                       # Wait a bit
    setSigGenModltn(HOST,PORT,AM_Mod)   # Select AM Modulation
    time.sleep(2)                       # Wait a bit
    setSigGenModltn(HOST,PORT,PM_Mod)   # Select PM Modulation
    time.sleep(2)                       # Wait a bit
    setSigGenModltn(HOST,PORT,FM_Mod)   # Select FM Modulation
    print("/------End of Setup signal generator---------/")

#%%   
# Main program
#-----------------------------------------------------------------------------    
print("/------Setup signal generator---------/")
setupSigGen()
