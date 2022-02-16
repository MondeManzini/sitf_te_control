import time
import unittest
from unittest import TestCase
from smb100a_sig_gen import initSigGen

# sig_gen_id = Rohde&Schwarz,SMB100A,1406.6000k02/102027,3.1.19.15-3.20.390.24 \n

class setupSigGenTest(TestCase):
    def initSigGenTest(self, sig_gen_id, set_state):
        self.assertEqual('Rohde&Schwarz,SMB100A,1406.6000k02/102027,3.1.19.15-3.20.390.24 \n', sig_gen_id)
        time.sleep(5)                   
        self.assertFalse(1, set_state)

    def setSigGenPowerTest(self, power):
        self.assertFalse(power, -25)
        time.sleep(5)                   
        self.assertTrue(power, -25)

    def setSigGenFreqTest(self, freq):
        self.assertFalse(freq, 1500e6)
        self.assertTrue(freq, 1500e6)

if __name__ == '__main__':
    unittest.main()