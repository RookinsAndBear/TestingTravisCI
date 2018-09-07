'''
    OrbitalElementsFromCartState.py
    Compute orbital elements from cartesian state vectors.

    INPUT: TBD
    OUTPUT: TBD

    METHOD LIST:    OrbitEnergyFromCartState
                    SemimajorAxisFromCartState
                    OrbitPeriodFromSma
'''

import math


def OrbitEnergyFromCartState(rMag, vMag, Gm):
    ''' OrbitEnergyFromCartState:
        INPUT:  rMag:   scalar position magnitude (meters)
                vMag:   scalar velocity magnitude (meters per second)
                Gm:     gravitational param (m^3/sec^2)

        OUTPUT: orbit energy from Cartesian state (m^2/s^2)
    '''

    if rMag == 0:
        raise ZeroDivisionError('Can not divide by zero')

    return (vMag**2 / 2) - Gm / rMag


def SemimajorAxisFromCartState(rMag, vMag, Gm):
    ''' OrbitEnergyFromCartState:
        INPUT:  rMag:   scalar position magnitude (meters)
                vMag:   scalar velocity magnitude (meters per second)
                Gm:     gravitational param (m^3/sec^2)

        OUTPUT: semimajor axis from Cartesian state (m)
    '''

    orbitEnergy = OrbitEnergyFromCartState(rMag, vMag, Gm)

    if orbitEnergy == 0:
        raise ZeroDivisionError('Can not divide by zero')

    SemimajorAxisFromCartState = -Gm / (2 * orbitEnergy)

    return SemimajorAxisFromCartState


def OrbitPeriodFromSma(sma, Gm):
    ''' OrbitPeriodFromSma:
        INPUT:  sma:    semimajor axis (m)
                Gm:     gravitational param (m^3/sec^2)

        OUTPUT: orbit period from semimajor axis (s)
    '''

    if Gm == 0:
        raise ZeroDivisionError('Can not divide by zero')

    if Gm < 0 or sma < 0:
        raise ValueError('Can not take a square root of a negative number')

    OrbitPeriodFromSma = 2 * math.pi * math.sqrt(sma**3 / Gm)

    if OrbitPeriodFromSma <= 0:
        raise ValueError('Orbit Period should not be negative or zero')

    return OrbitPeriodFromSma
