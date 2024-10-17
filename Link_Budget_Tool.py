import math
from case1 import Spacecraft, Payload, Requirement, Orbit, Ground_station

case_number = 1  # Input case number here (and change the import statement in line 2).

P_T = 10 * math.log10(Spacecraft.transmit_P)

def G_T(frequency):
    """Calculates G_T for a given (up-/downlink) frequency."""
    G_T = 20 * math.log10(Spacecraft.antenna_d) + 20 * math.log10(frequency) + 17.8  # Transmitter antenna gain [dB]
    return G_T

L_T = 10 * math.log10(Spacecraft.transmit_loss_f)  # Transmitter loss factor [dB]

def L_P(frequency):
    """Calculates L_P for a given (up-/downlink) frequency."""
    e_T = Orbit.pointing_offst  # Pointing offset [deg]
    alpha_half = 21 / (frequency * Spacecraft.antenna_d)  # deg

    L_P = 12 * ((e_T / alpha_half) ** 2)  # Pointing loss factor [dB]
    return L_P

def L_A():
    L_A = 0  # Atmospheric loss [dB] (I think we can neglect this since our frequency is low)
    return L_A

def L_FS(frequency):
    """Use only for LEO calculations. Calculates L_FS for a given (up-/downlink) frequency."""
    c = 3e8  # m/s
    Lambda = c / (frequency * 1e9)  # Wave length [m]
    R_E = 6371  # Earth radius [km]
    min_elev = math.radians(10)
    d = R_E * (math.sqrt(((Orbit.altitude + R_E) / R_E) ** 2 - (math.cos(min_elev)) ** 2) - math.sin(min_elev))  # km
    L_FS = 20 * math.log10((4 * math.pi * d * 1e3) / Lambda)  # dB
    return L_FS

def L_S(frequency):
    """Only use for interplanetary or deep-space missions. Calculates L_S for a given (up-/downlink) frequency."""
    c = 3e8  # m/s
    Lambda = c / (frequency * 1e9) # Wave length [m]
    theta_ES = math.radians(Orbit.elongation_angle)  # Elongation angle [rad]
    d_E = 149597870700  # Earth-Sun distance [km]
    d_S = Orbit.orbit_radius # Satellite-Sun distance [km]
    S = math.sqrt(d_E**2 + d_S**2 - (2 * d_E * d_S * math.cos(theta_ES)))
    L_S = (Lambda / (4 * math.pi * S))**2 # dB
    return L_S

L_R = 10 * math.log10(Ground_station.loss_factor)  # Receiver loss factor [dB]

def G_R(frequency):
    """Calculates G_R for a given (up-/downlink) frequency."""
    G_R = 20 * math.log10(Ground_station.antenna_d) + 20 * math.log10(frequency) + 17.8  # Receiver antenna gain [dB]
    return G_R

def T_s(case_number):
    if case_number == 1:
        T_s = 135  # Ground system noise temperature [K]
    elif case_number == 2:
        T_s = ...  # Ground system noise temperature [K]
    elif case_number == 3:
        T_s = ...  # Ground system noise temperature [K]
    elif case_number == 4:
        T_s = ...  # Ground system noise temperature [K]
    return T_s

def R():
    """Calculates R."""
    S_W = math.atan(Payload.width_angle / 2) * Orbit.altitude # Swath width [m]
    P_S = S_W / (Payload.width_angle / Payload.px_size)  # Pixel size [m]
    V = math.sqrt(Orbit.grav_param) / Orbit.radius  # Orbital velocity [m/s]
    R_G = Payload.bit_depth * (S_W * V) / (P_S ** 2)  # Generated data rate [bits/s]

    R = 10 * math.log10(R_G * (Payload.duty_cycle / Payload.downlink_fraction))  # Required data rate [dB]
    return R

def SNR(frequency):
    """Calculates SNR for a given (up-/downlink) frequency."""
    k = -228.6 # Boltzmann constant [dB]

    if case_number == 1 or case_number == 2:
        SNR = P_T + G_T(frequency) - L_T - L_A() - L_FS(frequency) - L_R + (G_R(frequency) / T_s()) - R() - k  # Signal to noise ratio [dB]
    if case_number == 3 or case_number == 4:
        SNR = P_T + G_T(frequency) - L_T - L_A() - L_S(frequency) - L_R + (G_R(frequency) / T_s()) - R() - k  # Signal to noise ratio [dB]
    return SNR

def margin(frequency):
    """Calculates the margin."""
    SNR_required = 10.5  # Required signal to noise ratio [dB]

    margin = SNR(frequency) - SNR_required  # Margin [dB] (must be larger than 3 dB)
    return margin