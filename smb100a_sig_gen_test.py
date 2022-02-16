import unittest
from unittest import TestCase

# sig_gen_id = Rohde&Schwarz,SMB100A,1406.6000k02/102027,3.1.19.15-3.20.390.24 \n

class setupSigGenTest(TestCase):
    def initSigGenTest(self, sig_gen_id, set_state):
        self.assertEqual(sig_gen_id, 'Rohde&Schwarz,SMB100A,1406.6000k02/102027,3.1.19.15-3.20.390.24 \n')
        self.assertFalse(set_state, 0)

    def setSigGenPowerTest(self, power):
        self.assertFalse(power, -25)
        self.assertTrue(power, 25)

    def setSigGenFreqTest(self, freq):
        self.assertFalse(freq, 1500e6)

if __name__ == '__main__':
    unittest.main()