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

import time
from sock_conn import s
# The script uses raw ethernet socket communication, and thus VISA library/installation is not required

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

# --------------Initialization of Variables---


def initSigGen():
    """
    Identify instrument. Can be used as a connectivity check
    """
    s.sendall(b'*IDN?\r\n')                             
    data = s.recv(1024)
    print('Received', data)
    sig_gen_id = data                           # for testing
    state=0
    setstate='OUTP1 {}\r\n'.format(state)       # Sets RF Output
    s.sendall(bytes(setstate, encoding='utf8'))
    s.sendall(b'OUTP1?\r\n')
    data=s.recv(1024)
    set_state = data                            # for testing
    print('Received', data)
    s.close()
    if data.decode('utf8')=='1\n':      # 
        print("RF Output On")
    else: print("RF Output Off")

def setSigGenPower(power):
    """
    This function sets the power of the signal generator
    Usage: 
        Power: float
    """
    setpower = 'POW {}\r\n'.format(power)
    s.sendall(bytes(setpower, encoding='utf8'))
    s.sendall(b'POW?\r\n')
    data = float(s.recv(1024))
    print("Sig gen power = %f dBm" %data)

def setSigGenFreq(Freq):
    """
    Identify instrument. Can be used as a connectivity check.
    """
    setfreq= "FREQ {}\r\n".format(Freq)
    s.sendall(bytes(setfreq, encoding='utf8'))
    s.sendall(b'FREQ?\r\n')
    data = float(s.recv(1024))
    #s.close()
    print(f"Sig gen frequency = {(data/1e6)} MHz")

def setSigGenState(state):
    """
    This function turns on/off the RF output state
    """
    setstate='OUTP1 {}\r\n'.format(state)
    s.sendall(bytes(setstate, encoding='utf8'))
    s.sendall(b'OUTP1?\r\n')
    data=s.recv(1024)
    print('Received', data)
    s.close()
    if data.decode("UTF-8") == "1\n":
        print("RF Output On")
    else: print(("RF Output Off"))

def setSigGenModsState(ModsState):
    setModsState='MOD:STAT {}\r\n'.format(ModsState)
    s.sendall(bytes(setModsState, encoding='utf8'))
    s.sendall(b'MOD:STAT?\n')
    data=s.recv(1024)
    print('Received', data)
    s.close()
    if data.decode("UTF-8") == "0\n":
        print("All modulations Off")
    else: print(("All modulations On"))


def setSigGenModltn(Modltn):
    """
    This function sets on different modulations:
    Usage:
        AM: string
        PM: string
        FM: string
    """
    setModState='{}:STAT?\r\n'.format(Modltn)
    s.sendall(bytes(setModState, encoding='utf8'))
    data=s.recv(1024)
    print('Received', data)
    s.close()
    if data.decode("UTF-8") == "1\n":
        print(f"{Modltn} Modulation On")
    else: print(f"{Modltn} Modulation On")

def setupSigGen():
    initSigGen()
    time.sleep(2)                       # Wait a bit
    setSigGenPower(Power)
    time.sleep(2)                       # Wait a bit
    setSigGenFreq(Freq)
    time.sleep(2)                       # Wait a bit
    setSigGenState(1)         # Turn on sig gen output
    time.sleep(2)                       # Wait a bit
    setSigGenModsState(OFF)  # Switch all modulations off
    time.sleep(2)                       # Wait a bit
    setSigGenModsState(ON)   # Switch all modulations on
    time.sleep(2)                       # Wait a bit
    setSigGenModltn(AM_Mod)   # Select AM Modulation
    time.sleep(5)                       # Wait a bit
    setSigGenModltn(PM_Mod)   # Select PM Modulation
    time.sleep(5)                       # Wait a bit
    setSigGenModltn(FM_Mod)   # Select FM Modulation
    print("/------End of Setup signal generator---------/")

#%%   
# Main program
#-----------------------------------------------------------------------------    
print("/------Setup signal generator---------/")
setupSigGen()
