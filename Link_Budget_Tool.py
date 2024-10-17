import math
from case2 import Spacecraft, Payload, Requirement, Orbit, Ground_station

case_number = 2  # Input case number here (and change the import statement in line 2).

P_T = 10 * math.log10(Spacecraft.transmit_P)  # Transmitter power [dBW]

def G_T(frequency):
    """Calculates G_T for a given (up-/downlink) frequency."""
    G_T = 20 * math.log10(Spacecraft.antenna_d) + 20 * math.log10(frequency) + 17.8  # Transmitter antenna gain [dB]

    return G_T

L_T = 10 * math.log10(Spacecraft.transmit_loss_f)  # Transmitter loss factor [dB]

def L_P(frequency):
    """Calculates L_P for a given (up-/downlink) frequency."""
    e_T = Orbit.pointing_offst  # Pointing offset [deg]
    alpha_half = 21 / (frequency * Spacecraft.antenna_d)  # [deg]

    L_P = 12 * ((e_T / alpha_half) ** 2)  # Pointing loss factor [dB]
    return L_P

def L_A(frequency):
    """Calculates L_A for a given (up-/downlink) frequency."""
    alpha = math.radians(10)  # Minimum elevation [deg]

    if frequency == Spacecraft.freq_downlink:
        L_A = Spacecraft.L_A0_down / math.sin(alpha)  # Atmospheric loss [dB]

    elif frequency == Spacecraft.freq_uplink:
        L_A = Spacecraft.L_A0_up / math.sin(alpha)  # Atmospheric loss [dB]

    return L_A

def L_FS(frequency):
    """Use only for LEO calculations. Calculates L_FS for a given (up-/downlink) frequency."""
    c = 3e8  # Speed of sound [m/s]
    Lambda = c / (frequency * 1e9)  # Wave length [m]
    R_E = 6371  # Earth radius [km]
    alpha = math.radians(10)  # Minimum elevation [deg]
    d = R_E * (math.sqrt(((Orbit.altitude + R_E) / R_E) ** 2 - (math.cos(alpha)) ** 2) - math.sin(alpha))  # Distance [km]

    L_FS = 20 * math.log10((4 * math.pi * d * 1e3) / Lambda)  # Free space loss [dB]

    return L_FS

def L_S(frequency):
    """Only use for interplanetary or deep-space missions. Calculates L_S for a given (up-/downlink) frequency."""
    c = 3e8  # Speed of sound [m/s]
    Lambda = c / (frequency * 1e9) # Wave length [m]
    theta_ES = math.radians(Orbit.elongation_angle)  # Elongation angle [rad]
    d_E = 149597870700 * 1e3  # Earth-Sun distance [m]
    d_S = Orbit.orbit_radius * 1e3  # Satellite-Sun distance [m]
    S = math.sqrt(d_E**2 + d_S**2 - (2 * d_E * d_S * math.cos(theta_ES)))  # [m]

    L_S = (Lambda / (4 * math.pi * S))**2 # Space loss [dB]

    return L_S

L_R = 10 * math.log10(Ground_station.loss_factor)  # Receiver loss factor [dB]

def G_R(frequency):
    """Calculates G_R for a given (up-/downlink) frequency."""
    G_R = 20 * math.log10(Ground_station.antenna_d) + 20 * math.log10(frequency) + 17.8  # Receiver antenna gain [dB]

    return G_R

def T_s(frequency):
    """Calculates T_s for a given (up-/downlink) frequency."""
    if frequency == Spacecraft.freq_downlink:
        T_s = Ground_station.T_s_down  # Ground system noise temperature [K]

    elif frequency == Spacecraft.freq_uplink:
        T_s = Ground_station.T_s_up  # Ground system noise temperature [K]

    return T_s

def R(frequency):
    """Calculates R for a given (up-/downlink) frequency."""
    if frequency == Spacecraft.freq_downlink:
        S_W = math.atan(Payload.width_angle / 2) * Orbit.altitude # Swath width [m]
        P_S = S_W / (Payload.width_angle / Payload.px_size)  # Pixel size [m]
        V = math.sqrt(Orbit.grav_param) / Orbit.radius  # Orbital velocity [m/s]
        R_G = Payload.bit_depth * (S_W * V) / (P_S ** 2)  # Generated data rate [bits/s]

        R = 10 * math.log10(R_G * (Payload.duty_cycle / Payload.downlink_fraction))  # Required data rate [dB]

    elif frequency == Spacecraft.freq_uplink:
        R = 10 * math.log10(Requirement.uplink_data_rate)  # Required data rate [dB]

    return R

def SNR(frequency):
    """Calculates SNR for a given (up-/downlink) frequency."""
    k_B = -228.6 # Boltzmann constant [dB]

    if case_number == 1 or case_number == 2:
        SNR = P_T + G_T(frequency) - L_T - L_A(frequency) - L_FS(frequency) - L_R + (G_R(frequency) / T_s(frequency)) - R(frequency) - k_B  # Signal-to-noise ratio [dB]

    if case_number == 3 or case_number == 4:
        SNR = P_T + G_T(frequency) - L_T - L_A(frequency) - L_S(frequency) - L_R + (G_R(frequency) / T_s(frequency)) - R(frequency) - k_B  # Signal-to-noise ratio [dB]

    return SNR

def SNR_margin(frequency):
    """Calculates the margin."""
    SNR_required = 10.5  # Required signal-to-noise ratio [dB]

    SNR_margin = SNR(frequency) - SNR_required  # Signal-to-noise ratio margin [dB] (must be larger than 3 dB)

    return SNR_margin

print(f"The downlink signal-to-noise ratio = {SNR(Spacecraft.freq_downlink)} dB\n"
      f"The uplink signal-to-noise ratio = {SNR(Spacecraft.freq_uplink)} dB\n"
      f"The required up-/downlink signal-to-noise ratio = 10.5 dB\n"
      f"The downlink signal-to-noise ratio margin = {SNR_margin(Spacecraft.freq_downlink)} dB\n"
      f"The uplink signal-to-noise ratio margin = {SNR_margin(Spacecraft.freq_uplink)} dB")