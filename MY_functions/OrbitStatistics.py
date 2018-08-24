''' OrbitStatistics.py
    Generate covariance matrix, standard deviation, etc.

    INPUT: TBD
    OUTPUT: TBD

    METHOD LIST:    CartCovSymmetricFromCartCovSTK
                    ComputePeriodCovFromCartCov
                    TransformCovarianceScalar
'''
import math
import numpy as np
from numpy import linalg as la
import OrbitalElementsFromCartState

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


def TransformCovarianceScalar(C1, M):   
    ''' TransformCovarianceScalar: 
        INPUT:  C1:  covariance matrix C1 in one coord system
                M:   transformation matrix M from C1
            
        OUTPUT: C2: scalar covariance in the second coord system as C2 = M*C1*M'
    '''

    C2 = M*C1.astype(np.float)*M.reshape(6,1)
    return C2