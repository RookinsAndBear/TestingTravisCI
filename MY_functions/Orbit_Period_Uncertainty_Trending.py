''' Orbit_Period_Uncertainty_Trending.py 

INPUT:  ephemeris file name (example.e found in adam_home/data/ephem)
        reference time for analysis (from epoch in seconds)

OUTPUT: period uncertainty 1-sigma standard deviation (seconds)

METHOD LIST:    odtk_ExtractPosVelCov
                dummy_ExtractPosVelCov
                CartCovSymmetricFromCartCovSTK
                ComputePeriodCovFromCartCov
                OrbitEnergyFromCartState
                SemimajorAxisFromCartState
                OrbitPeriodFromSma
                TransformCovarianceScalar

'''

import math
import numpy as np
from numpy import linalg as la

def odtk_ExtractPosVelCov(ephemFile, ref_time):
    ''' odtk_ExtractPosVelCov:  Search ephemeris file for reference time and extract Time, Pos, Vel, Lower Tri Cov Matrix

        INPUT:  ephemFile:      string path and file name
                ref_time:       integer reference time to search for (sec)

        OUTPUT: values_stk:     STK data matrix [28 x 1]:
                                7 x 1  time, position, velocity
                                21 x 1 state covariance matrix lower triangular format      
    '''
    f = open(ephemFile,'r')
    lines = f.readlines()
    count = 0; linenum = 0; convertTime = 0

    for x in lines:
        linenum = linenum + 1
        if x.split(' ')[0].find("e+") == -1:
            pass
        else:
            convertTime = str(int(float("{:.8f}".format(float(x.split(' ')[0])))))

        if convertTime == ref_time and len(x.split(' ')) > 1:
            count = count + 1
            if count == 1:
                TimePosVel = x.split(' ')
            if count == 2:
                Cov_1 = x.split(' ')
                Cov_2 = lines[linenum].split(' ')
                Cov_2 = Cov_2[22:len(Cov_2)]
                Cov_3 = lines[linenum+1].split(' ')
                Cov_3 = Cov_3[22:len(Cov_3)]


    f.close()
    values_stk = [TimePosVel[0],TimePosVel[1],TimePosVel[2],TimePosVel[3],TimePosVel[4],TimePosVel[5],TimePosVel[6],
                       Cov_1[1],Cov_1[2],Cov_1[3],Cov_1[4],Cov_1[5],Cov_1[6],Cov_1[7],
                       Cov_2[0],Cov_2[1],Cov_2[2],Cov_2[3],Cov_2[4],Cov_2[5],Cov_2[6],
                       Cov_3[0],Cov_3[1],Cov_3[2],Cov_3[3],Cov_3[4],Cov_3[5],Cov_3[6]]

    return values_stk

def dummy_ExtractPosVelCov(ephemFile, ref_time):
    ''' dummy_ExtractPosVelCov: demo STK visualiztion ipynb STK .e file format - testing purposes
                                original file does not contain covariance matrix.
                                Search ephemeris file for reference time and extract Time, Pos, Vel, Lower Tri Cov Matrix

        INPUT:  ephemFile:      string path and file name
                ref_time:       integer reference time to search for (sec)

        OUTPUT: values_stk:     STK data matrix [28 x 1]:
                                7 x 1  time, position, velocity
                                21 x 1 state covariance matrix lower triangular format      
    '''
    # read ephem file
    lines = []
    with open(ephemFile, 'r') as f:
        for line in f:
            lines.append(line)
        for linenum, line in enumerate(lines):
            str = lines[linenum]
            if str.find(ref_time) == 0:
                values_stk = str.split('\t') # dummy ephem file uses tabs from importing into Excel
                #values = str.split(' ') # real ephem files use spaces
    f.close()

    return values_stk

def CartCovSymmetricFromCartCovSTK(CartCov_stk):
    ''' CartCovSymmetricFromCartCovSTK
        INPUT: CartCov_stk:     STK data matrix [28 x 1]:
                                7 x 1  time, position, velocity [not used in this method]
                                21 x 1 state covariance matrix lower triangular format

        OUTPUT: CartCov:        6 by 6 state symmetric covariance (upper triangle filled by symmetry)
    '''

    CartCov =  np.matrix([
                         [CartCov_stk[7],    CartCov_stk[8],    CartCov_stk[10],    CartCov_stk[13],    CartCov_stk[17],    CartCov_stk[22]],
                         [CartCov_stk[8],    CartCov_stk[9],    CartCov_stk[11],    CartCov_stk[14],    CartCov_stk[18],    CartCov_stk[23]],
                         [CartCov_stk[10],   CartCov_stk[11],   CartCov_stk[12],    CartCov_stk[15],    CartCov_stk[19],    CartCov_stk[24]],
                         [CartCov_stk[13],   CartCov_stk[14],   CartCov_stk[15],    CartCov_stk[16],    CartCov_stk[20],    CartCov_stk[25]],
                         [CartCov_stk[17],   CartCov_stk[18],   CartCov_stk[19],    CartCov_stk[20],    CartCov_stk[21],    CartCov_stk[26]],
                         [CartCov_stk[22],   CartCov_stk[23],   CartCov_stk[24],    CartCov_stk[25],    CartCov_stk[26],    CartCov_stk[27]]
                         ])

    return CartCov

def ComputePeriodCovFromCartCov(pos, vel, CartCov_6x6, Gm):
    ''' ComputePeriodCovFromCartCov
        INPUT:  pos:            1 x 3 position at reference time x,y,z (meters)
                vel:            1 x 3 velocity at reference time x_dot, y_dot, z_dot (meters per second)
                CartCov_6x6:    6 by 6 state symmetric covariance
                Gm:             gravitational param (m^3/sec^2)
            
        OUTPUT: scalar covariance in second coord system
    '''
    vMag = la.norm(vel)
    rMag = la.norm(pos)
    orbitEnergy = OrbitEnergyFromCartState(rMag, vMag, Gm) 
    sma = SemimajorAxisFromCartState(rMag, vMag, Gm) #can pass in orbit energy but want to keep method 'generic'
    orbitPeriod = OrbitPeriodFromSma(sma, Gm)
    #print('Orbit Period (sec): ', orbitPeriod)
    #print('Orbit Period (days): ', orbitPeriod/86400)

    coeff = -1.5 * (orbitPeriod / orbitEnergy)
    
    #    'deriv with respect to position
    DPeriodDCartState = []
    for idx, val in enumerate(pos):
        # elements 0,1,2
        DPeriodDCartState.append(coeff * Gm / rMag**3  * float(val))

    #    'deriv with respect to velocity
    for idx, val in enumerate(vel):
        # elements 3,4,5
        DPeriodDCartState.append(coeff * float(val))

 #    'The Period covariance is given by matrix multiplication DPeriodDCartState * CartCov * DPeriodDCartState'
 #    'where prime indicates transpose
    DPeriodDCartState = np.matrix(DPeriodDCartState)

    return TransformCovarianceScalar(CartCov_6x6, DPeriodDCartState)

def OrbitEnergyFromCartState(rMag, vMag, Gm):
    ''' OrbitEnergyFromCartState: 
        INPUT:  rMag:   scalar position magnitude (meters)
                vMag:    scalar velocity magnitude (meters per second)
                Gm:     gravitational param (m^3/sec^2)
            
        OUTPUT: orbit energy from Cartesian state (m^2/s^2)
    '''
                
    return (vMag**2 / 2)  - Gm / rMag


def SemimajorAxisFromCartState(rMag, vMag, Gm):
    ''' OrbitEnergyFromCartState: 
        INPUT:  rMag:   scalar position magnitude (meters)
                vMag:    scalar velocity magnitude (meters per second)
                Gm:     gravitational param (m^3/sec^2)
            
        OUTPUT: semimajor axis from Cartesian state (m)
    '''
    
    orbitEnergy = OrbitEnergyFromCartState(rMag, vMag, Gm)
    SemimajorAxisFromCartState = -Gm / (2 * orbitEnergy)

    return SemimajorAxisFromCartState    

def OrbitPeriodFromSma(sma, Gm): 
    ''' OrbitPeriodFromSma: 
        INPUT:  sma:    semimajor axis (m)
                Gm:     gravitational param (m^3/sec^2)
            
        OUTPUT: orbit period from semimajor axis (s)
    '''
    
    OrbitPeriodFromSma = 2 * math.pi * math.sqrt(sma**3 / Gm)
    return OrbitPeriodFromSma

def TransformCovarianceScalar(C1, M):   
    ''' TransformCovarianceScalar: 
        INPUT:  C1:  covariance matrix C1 in one coord system
                M:   transformation matrix M from C1
            
        OUTPUT: C2: scalar covariance in the second coord system as C2 = M*C1*M'
    '''

    C2 = M*C1.astype(np.float)*M.reshape(6,1)
    return C2
