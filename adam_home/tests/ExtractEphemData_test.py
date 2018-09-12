'''
    test_ExtractEphemData.py
    Unit test module

    from terminal: home/adam_home/tests
                   python -m unittest test_ExtractEphemData.py

                   OR

                   home/adam_home/tests
                   python test_ExtractEphemData.py
                   [when if __name__ block is available on line 64]

    METHOD LIST:    test_dummy_ExtractPosVelCov
                    test_odtk_ExtractPosVelCov
'''

import unittest
import ExtractEphemData
import sys
from os.path import expanduser
sys.path.append(expanduser("~") + "/adam_home/SEE_functions")


class Test_ExtractEphemData(unittest.TestCase):

    def test_dummy_ExtractPosVelCov(self):
        # ephem_file = expanduser("~") + '/adam_home/data/ephem' + '/dummy_ephem.e'
        ephem_file = '/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/data/ephem' + '/dummy_ephem.e'

        values_stk = ['29808000',
                      '200705138.8', '-188817438.9', '-49873952.76', '736.5850035', '-2', '370.4811842',
                      '20174685.75', '1.60E+07', '17287242.7', '1.83E+07', '1.06E+07', '5.49E+07', '-2.18E+01',
                      '-1.26E+01', '9.36E+00', '1.60E-04', '7.45E+01', '5.79E+01', '2.11E+02', '1.38E-04',
                      '1.05E-03', '2.75E+01', '4.25E+01', '-1.03E+01', '-1.25E-04', '-1.90E-04', '4.07E-04\n']

        self.assertEqual(ExtractEphemData.dummy_ExtractPosVelCov(ephem_file, '29808000'), values_stk)

        # Error handling
        # option 1:
        # self.assertRaises(ZeroDivisionError, ExtractEphemData.odtk_ExtractPosVelCov, 16, 0)
        # option 2: use context manager
        # with self.assertRaises(ZeroDivisionError):
        # ExtractEphemData.odtk_ExtractPosVelCov(175521278.778045,0)

        with self.assertRaises(ValueError):
            ExtractEphemData.dummy_ExtractPosVelCov(ephem_file, '2.9808000e+7')

        with self.assertRaises(FileNotFoundError):
            # ephem_file = expanduser("~") + '/adam_home/data/ephem' + '/missing_dummy_ephem.e'
            ephem_file = '/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/data/ephem' + '/missing_dummy_ephem.e'
            ExtractEphemData.dummy_ExtractPosVelCov(ephem_file, '196')

    def test_odtk_ExtractPosVelCov(self):
        # ephem_file = expanduser("~") + '/adam_home/data/ephem' + '/modified_dummy.e'
        ephem_file = '/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/data/ephem' + '/modified_dummy.e'

        values_stk = ['5.60600000000000e+03',
                      '4.07696263873150e+07', '-1.70809904449045e+08', '-9.66331679556395e+07',
                      '1.57060063751855e+02', '1.13298048038556e+03', '3.89289745227734e+02\n',
                      '1.05439097338782e+04', '-2.34492974147408e+03', '4.64345657396604e+03',
                      '-3.14822202715566e+03', '6.06902201170811e+01', '4.29976728639937e+03',
                      '-4.21413200898710e-02\n',
                      '3.35105510396153e-02', '2.13465219181365e-02', '3.95118694344618e-07',
                      '-3.28871551875770e-02', '8.58497071571136e-04', '1.61123365254981e-02',
                      '8.10171502110303e-08\n',
                      '1.77536195738882e-07', '4.21462146377177e-02', '1.97961560364326e-02',
                      '-2.51847242620078e-02', '-2.47329891882243e-09', '-2.05478115461443e-07',
                      '4.63398878632980e-07\n']

        self.assertEqual(ExtractEphemData.odtk_ExtractPosVelCov(ephem_file, '5606'), values_stk)

        # Error handling
        # option 1:
        # self.assertRaises(ZeroDivisionError, ExtractEphemData.odtk_ExtractPosVelCov, 16, 0)
        # option 2: use context manager
        # with self.assertRaises(ZeroDivisionError):
        # ExtractEphemData.odtk_ExtractPosVelCov(175521278.778045,0)

        with self.assertRaises(ValueError):
            ExtractEphemData.odtk_ExtractPosVelCov(ephem_file, '5.60600000000000e+03')

        with self.assertRaises(FileNotFoundError):
            ephem_file = expanduser("~") + '/adam_home/data/ephem' + '/missing_dummy_ephem.e'
            ExtractEphemData.odtk_ExtractPosVelCov(ephem_file, '196')


if __name__ == '__main__':
    unittest.main()
