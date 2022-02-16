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

Zero = 0
One = 1
OFF = 'OFF'
ON = 'ON'
AM_Mod = 'AM'
FM_Mod = 'FM'
PM_Mod = 'PM'
# --------------------------------------------

# --------------Initialization of Variables---
Power = 0                                 
Freq = 0                

def initSigGen():
    """
    This function establishes a socket connection and identifies the instrument
    @params     : None
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

def setSigGenState(RFOut):
    """
    This function turns on/off the RF output state
    """
    setstate='OUTP1 {}\r\n'.format(RFOut)
    s.sendall(bytes(setstate, encoding='utf8'))
    s.sendall(b'OUTP1?\r\n')
    data=s.recv(1024)
    print('Received', data)
    s.close()
    if data.decode("UTF-8") == "1\n":
        print("RF Output On")
    else: print(("RF Output Off"))

def setSigGenModsState(ModsState):
    """
    This function sets all modulation modes off
    @param ModsState: String
    """
    setModsState='MOD:STAT {}\r\n'.format(ModsState)
    s.sendall(bytes(setModsState, encoding='utf8'))
    s.sendall(b'MOD:STAT?\n')
    data=s.recv(1024)
    print('Received', data)
    s.close()
    if data.decode("UTF-8") == "0\n":
        print("All modulations Off")
    else: print(("All modulations On"))

# ---------------------Modulations State Function-----------------------
def setSigGenModState(ModState):
    """
    This function sets on different modulation schemes:
    @param  AM: string /
            PM: string /
            FM: string
    """
    setModState='{}:STAT?\r\n'.format(ModState)
    s.sendall(bytes(setModState, encoding='utf8'))
    data=s.recv(1024)
    print('Received', data)
    s.close()
    if data.decode("UTF-8") == "1\n":
        print(f"{ModState} Modulation On")
    else: print(f"{ModState} Modulation On")

# ---------------------Main Function-----------------------------------

def setupSigGen():
    initSigGen()                    # Get instrument ID
    time.sleep(5)                   # Wait a bit
    setSigGenPower(Power)           # Set the power to 0dBm
    time.sleep(5)                   # Wait a bit
    setSigGenPower(-25)             # Set the power to -25dBm
    time.sleep(5)                   # Wait a bit
    setSigGenFreq(Freq)             # Set the power to 0Hz
    time.sleep(5)                   # Wait a bit
    setSigGenFreq(1500e6)           # Set the power to 1.5GHz
    time.sleep(5)                   # Wait a bit
    setSigGenState(Zero)            # Turn on sig gen output
    time.sleep(5)                   # Wait a bit
    setSigGenState(One)             # Turn on sig gen output
    time.sleep(5)                   # Wait a bit
    setSigGenModsState(OFF)         # Switch all modulations off
    time.sleep(5)                   # Wait a bit
    setSigGenModsState(ON)          # Switch all modulations on
    time.sleep(5)                   # Wait a bit
    setSigGenModState(AM_Mod)       # Select AM Modulation
    time.sleep(5)                   # Wait a bit
    setSigGenModState(PM_Mod)       # Select PM Modulation
    time.sleep(5)                   # Wait a bit
    setSigGenModState(FM_Mod)       # Select FM Modulation
    print("/------End of Setup signal generator---------/")

#%%   
# Main program
#-----------------------------------------------------------------------------    
print("/------Setup signal generator---------/")
setupSigGen()
