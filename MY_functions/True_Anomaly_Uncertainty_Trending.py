''' True Anomaly Uncertainty Trending '''
# --------------------------------------------------------------
# HEADER PATH/FILE/PACKAGE SETUP
# --------------------------------------------------------------
# No need to import adam or use tokens
import sys, os, math
import numpy as np
from os.path import expanduser
# set standard SEE data/ephem file path
ephem_path = expanduser("~") + "/adam_home/data/ephem"  # / syntax works for Windows, Mac, and Linux
sys.path.append(ephem_path)

ephem_file = '/dummy_ephem.e'

# --------------------------------------------------------------
# Function definitions
# --------------------------------------------------------------
        
    #'CartCovSymmetricFromCartCovSTK takes in a state covariance matrix in 3 by 7 STK lower triangular format and produces a
    #'6 by 6 state symmetric covariance
def CartCovSymmetricFromCartCovSTK(CartCov_stk):
    #'fill lower triangle and fill upper triangle by symmetry 
    CartCov =  np.matrix([[CartCov_stk[7],    CartCov_stk[8],    CartCov_stk[10],    CartCov_stk[13],    CartCov_stk[17],    CartCov_stk[22]],
                         [CartCov_stk[8],    CartCov_stk[9],    CartCov_stk[11],    CartCov_stk[14],    CartCov_stk[18],    CartCov_stk[23]],
                         [CartCov_stk[10],   CartCov_stk[11],   CartCov_stk[12],    CartCov_stk[15],    CartCov_stk[19],    CartCov_stk[24]],
                         [CartCov_stk[13],   CartCov_stk[14],   CartCov_stk[15],    CartCov_stk[16],    CartCov_stk[20],    CartCov_stk[25]],
                         [CartCov_stk[17],   CartCov_stk[18],   CartCov_stk[19],    CartCov_stk[20],    CartCov_stk[21],    CartCov_stk[26]],
                         [CartCov_stk[22],   CartCov_stk[23],   CartCov_stk[24],    CartCov_stk[25],    CartCov_stk[26],    CartCov_stk[27]]])

    return CartCov

def ComputePeriodCovFromCartCov(pos, vel, CartCov_6x6, Gm):

    orbitEnergy = OrbitEnergyFromCartState(pos, vel, Gm)
    sma = SemimajorAxisFromCartState(pos, vel, Gm)
    orbitPeriod = OrbitPeriodFromSma(sma, Gm)
    print('Orbit Period (sec): ', orbitPeriod)
    print('Orbit Period (days): ', orbitPeriod/86400)

    coeff = -1.5 * (orbitPeriod / orbitEnergy)
    rMag = VectorNorm(pos)
    
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
    
#'Function OrbitEnergyFromCartState computes orbit energy from Cartesian state
def OrbitEnergyFromCartState(pos, vel, Gm):
 
    vMag = VectorNorm(vel)
    rMag = VectorNorm(pos)
                
    return (vMag**2 / 2)  - Gm / rMag
        
#'VectorNorm computes the norm of a vector
def VectorNorm(a):
    norm = 0
    for i in a:
        norm = norm + float(i) * float(i)

    return math.sqrt(norm)

#'SemimajorAxisFromCartState computes semimajor axis from Cartesian state
def SemimajorAxisFromCartState(pos, vel, Gm):
    
    orbitEnergy = OrbitEnergyFromCartState(pos, vel, Gm)
    SemimajorAxisFromCartState = -Gm / (2 * orbitEnergy)

    return SemimajorAxisFromCartState    

#'OrbitPeriodFromSma computes orbit period from semimajor axis
#'Minimum returns the minimum of two numbers
def OrbitPeriodFromSma(sma, Gm): 
    
    OrbitPeriodFromSma = 2 * math.pi * math.sqrt(sma**3 / Gm)
    return OrbitPeriodFromSma

#'TransformCovarianceScalar takes in a covariance matrix C1 in one coord system and
#'a transformation matrix M from that coord system into a scalar
#'The function returns the covariance in the second coord system as C2 = M*C1*M'
def TransformCovarianceScalar(C1, M):   

    C2 = M*C1.astype(np.float)*M.reshape(6,1)
    return C2

def ComputeEccentricityFromCartState(pos, vel, Gm):
    ''' ComputeEccentricityFromCartState
        INPUT:  pos:            1 x 3 position at reference time x,y,z (meters)
                vel:            1 x 3 velocity at reference time x_dot, y_dot, z_dot (meters per second)
                Gm:             gravitational param (m^3/sec^2)
            
        OUTPUT: e_vec: 1x= x 3 eccentricity vector
    '''
    #ER =6378.1370# 3.986004415 * 10**5
    #TU = 806.80415
    #pos = ([6524.834/6378.1370,6862.875/6378.1370,6448.296/6378.1370])
    #pos=([1.023, 1.076, 1.011])
    pos_array = np.array(pos,dtype=float)
    #print(pos_array)
    rMag = VectorNorm(pos_array)
    #print(rMag)
    #print(pos_array.shape)
    #print(pos_array)
    #vel = ([4.901327/(6378.1370/806.8), 5.533756/(6378.1370/806.8), -1.976341/(6378.1370/806.8)])
    #vel = ([.62, .7, -.25])
    vel_array = np.array(vel,dtype=float)
    vMag = VectorNorm(vel_array)
    #print(vMag)
    #print(vel_array.shape)
    #print(vel_array)
    #vMag = .967936
    #rMag = VectorNorm(pos)
    #rMag = 1.796226
    #print(rMag)
    #evec = ((mag(v)^2-mu/mag(r))*r-dot(r,v)*v)/mu
    elem1 = []
    for idx, val in enumerate(pos_array):
        # elements 0,1,2
        elem1.append((vMag**2 - (Gm/rMag))* float(val))

    #pos_array = np.array(pos)
    #print(pos_array)
    #print(pos_array.shape)
    #vel_array = np.array(vel)
    #print(vel_array)
    #print(vel_array.shape)
    #mu = (ER**3)/TU**2
    #print(mu)
    #scalar = np.array([vMag**2 - (Gm/rMag),vMag**2 - (Gm/rMag),vMag**2 - (Gm/rMag)])[:,None]
    #print(scalar)
    #print(pos_array)
    #elem1 = scalar * pos_array
    #print(elem1)
    #elem1 = np.array((vMag**2 - (mu/rMag))* pos_array)

    elem2 = (pos_array.dot(vel_array.transpose()))*vel_array

    return  (1/Gm)*(elem1 - elem2)#(1/mu)*(np.array((vMag**2 - (mu/rMag))* pos_array) - (pos_array.dot(vel_array.transpose()))*vel_array)#(1/mu)*(elem1 - elem2)#(1/Gm)*(elem1 - elem2)

def ComputeTrueAnomaly(e_vec, eMag, pos, vel):
    pos_array = np.array(pos, dtype=float)
    #print(pos_array)
    vel_array = np.array(vel, dtype=float)
    #print(vel_array)
    rMag = VectorNorm(pos_array)

    #print(rMag)
    #print(eMag)
    e_array = np.array(e_vec,dtype=float)
    #print(e_vec.dot(pos_array))
    nu = math.acos((e_array.dot(pos_array))/(eMag*rMag)) # degrees
    #print('nu: ', nu)
    if (pos_array.dot(vel_array)) < 0:
        #print(pos_array.dot(vel_array))
        nu = 360-nu

    return  nu
# --------------------------------------------------------------
# MAIN ROUTINE
# Part 1
# Read in STK .e file, enter the time and pull out
# the corresponding position, velocity, and covariance data.
# Compute the orbit period uncertainty
# --------------------------------------------------------------

# User sets the reference time for analysis (sec)
#ref_time = str(29808000) # epoch sec cast to string
# gravitational param (m^3/sec^2)
#Gm = 398600.5*1000000000
#lines= []

# read ephem file
#with open(ephem_path + ephem_file, 'r') as f:
#    for line in f:
#        lines.append(line)
#    for linenum, line in enumerate(lines):
#        str = lines[linenum]
#        if str.find(ref_time) == 0:
#            values_stk = str.split('\t') # dummy ephem file uses tabs from importing into Excel
#            #values = str.split(' ') # real ephem files use spaces

#            TimePosVel = (
#                            [values_stk[0]],
#                            [values_stk[1], values_stk[2], values_stk[3]],
#                            [values_stk[4], values_stk[5], values_stk[6]]
#                         )



#CartCov_6x6 = CartCovSymmetricFromCartCovSTK(values_stk)

#PeriodCov = ComputePeriodCovFromCartCov(TimePosVel[1], TimePosVel[2], CartCov_6x6, Gm)

#PeriodStdDev = math.sqrt(PeriodCov)

#print('Period Uncertainty 1-sigma StdDev (sec): ',PeriodStdDev)

#e_vec = ComputeEccentricityFromCartState(TimePosVel[1],  TimePosVel[2], Gm)
#print(e_vec)
#eMag = VectorNorm(e_vec)
#print(eMag)

#trueAnomaly = ComputeTrueAnomaly(e_vec, eMag, TimePosVel[1], TimePosVel[2])
#print('trueAnomaly: ',trueAnomaly )
# Part 2
# Compute uncertaint in true anomaly.
# Essentially the "degrees" version of orbit period.
