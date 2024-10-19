import math
from case4 import Spacecraft, Payload, Requirement, Orbit, Ground_station

case_number = 4  # Input case number here (and change the import statement in line 2).

def P_T(frequency):
    """Calculates P_T for a given (up-/downlink) frequency."""
    if frequency == Spacecraft.freq_downlink:
        P_T = 10 * math.log10(Spacecraft.transmit_P)  # Spacecraft transmitter power [dBW]

    elif frequency == Spacecraft.freq_uplink:
        P_T = 10 * math.log10(Ground_station.transmit_P)  # Ground station transmitter power [dBW]

    return P_T

def G_T(frequency):
    """Calculates G_T for a given (up-/downlink) frequency."""
    if frequency == Spacecraft.freq_downlink:
        G_T = 20 * math.log10(Spacecraft.antenna_d) + 20 * math.log10(frequency) + 17.8  # Spacecraft transmitter antenna gain [dB]

    elif frequency == Spacecraft.freq_uplink:
        G_T = 20 * math.log10(Ground_station.antenna_d) + 20 * math.log10(frequency) + 17.8  # Ground station transmitter antenna gain [dB]

    return G_T

L_TS = 10 * math.log10(Spacecraft.transmit_loss_f)  # Spacecraft transmitter loss factor[dB]
L_TG = 10 * math.log10(Ground_station.loss_factor)  # Ground station transmission loss factor [dB]

def L_P(frequency):
    """Calculates L_P for a given (up-/downlink) frequency."""
    if frequency == Spacecraft.freq_downlink:
        alpha_half_T = 21 / (frequency * Spacecraft.antenna_d)  # Transmitter half power angle [deg]
        alpha_half_R = 21 / (frequency * Ground_station.antenna_d)  # Receiver half power angle [deg]
        e_T = Orbit.pointing_offst  # Transmitter pointing offset [deg]
        e_R = 0.1 * alpha_half_R  # Receiver pointing offset [deg]

        L_P = - ((12 * ((e_T / alpha_half_T) ** 2)) + (12 * ((e_R / alpha_half_R) ** 2)))  # Downlink pointing loss factor [dB]

    elif frequency == Spacecraft.freq_uplink:
        alpha_half_T = 21 / (frequency * Ground_station.antenna_d)  # Transmitter half power angle [deg]
        alpha_half_R = 21 / (frequency * Spacecraft.antenna_d)  # Receiver half power angle [deg]
        e_T = 0.1 * alpha_half_T  # Transmitter pointing offset [deg]
        e_R = Orbit.pointing_offst  # Receiver pointing offset [deg]

        L_P = - ((12 * ((e_T / alpha_half_T) ** 2)) + (12 * ((e_R / alpha_half_R) ** 2)))  # Uplink pointing loss factor [dB]

    return L_P

def L_A(frequency):
    """Calculates L_A for a given (up-/downlink) frequency."""
    alpha = math.radians(10)  # Minimum elevation [deg]

    if frequency == Spacecraft.freq_downlink:
        L_A = - (Spacecraft.L_A0_down / math.sin(alpha))  # Downlink atmospheric loss [dB]

    elif frequency == Spacecraft.freq_uplink:
        L_A = - (Spacecraft.L_A0_up / math.sin(alpha))  # Uplink atmospheric loss [dB]

    return L_A

def L_FS(frequency):
    """Use only for LEO calculations. Calculates L_FS for a given (up-/downlink) frequency."""
    c = 3e8  # Speed of light [m/s]
    alpha = math.radians(10)  # Minimum elevation [deg]
    R_E = 6371000  # Earth radius [m]R_E = 6371000  # Earth radius [m]

    Lambda = c / (frequency * 1e9)  # Wave length [m]

    Lambda = c / (frequency * 1e9)  # Wave length [m]
    d = R_E * (math.sqrt(((Orbit.altitude + R_E) / R_E) ** 2 - (math.cos(alpha)) ** 2) - math.sin(alpha))  # Distance [km]

    L_FS = - (20 * math.log10((4 * math.pi * d * 1e3) / Lambda))  # Free space loss [dB]

    elif case_number == 2:
        d = R_E * (math.sqrt(((Orbit.altitude + 384400000 + 1737400 + R_E) / R_E) ** 2 - (math.cos(alpha)) ** 2) - math.sin(alpha))  # Distance [m]

        L_FS = - (20 * math.log10((4 * math.pi * d) / Lambda))  # Free space loss [dB]
    return L_FS

def L_S(frequency):
    """Only use for interplanetary or deep-space missions. Calculates L_S for a given (up-/downlink) frequency."""
    c = 3e8  # Speed of light [m/s]
    d_E = 1.496e+11 # Earth-Sun distance [m]
    d_S = Orbit.orbit_radius * 1e3  # Satellite-Sun distance [m]

    Lambda = c / (frequency * 1e9)  # Wave length [m]
    S = math.sqrt(d_E**2 + d_S**2 - (2 * d_E * d_S * math.cos(Orbit.elongation_angle)))  # [m]
    L_S = 10 * math.log10((Lambda / (4 * math.pi * S))**2) # Space loss [dB]

    return L_S

def G_R(frequency):
    """Calculates G_R for a given (up-/downlink) frequency."""
    if frequency == Spacecraft.freq_downlink:
        G_R = 20 * math.log10(Ground_station.antenna_d) + 20 * math.log10(frequency) + 17.8  # Downlink receiver antenna gain [dB]

    elif frequency == Spacecraft.freq_uplink:
        G_R = 20 * math.log10(Spacecraft.antenna_d) + 20 * math.log10(frequency) + 17.8  # Uplink receiver antenna gain [dB]

    return G_R

def T_s(frequency):
    """Calculates T_s for a given (up-/downlink) frequency."""
    if frequency == Spacecraft.freq_downlink:
        T_s = 10 * math.log10(Ground_station.T_s_down)  # Downlink ground system noise temperature [K]

    elif frequency == Spacecraft.freq_uplink:
        T_s = 10 * math.log10(Ground_station.T_s_up)  # Uplink ground system noise temperature [K]

    return T_s

def R(frequency):
    """Calculates R for a given (up-/downlink) frequency."""
    if frequency == Spacecraft.freq_downlink:
        S_W = math.tan(Payload.width_angle / 2) * Orbit.altitude * 2 # Swath width [m]
        P_S = math.tan(Payload.px_size) * Orbit.altitude  # Pixel size [m]
        V = math.sqrt(Orbit.grav_param) / Orbit.radius  # Orbital velocity [m/s]
        R_G = Payload.bit_depth * (S_W * V) / (P_S ** 2)  # Generated data rate [bits/s]

        R = 10 * math.log10(2 * R_G * (Payload.duty_cycle / Payload.downlink_fraction))  # Downlink required data rate [dBbits/s]

    elif frequency == Spacecraft.freq_uplink:
        R = 10 * math.log10(2 * Requirement.uplink_data_rate)  # Uplink required data rate [dBbits/s]

    return R

k_B = 10 * math.log10(1.380649e-23) # Boltzmann constant [dBJ/K]
def SNR(frequency):
    """Calculates SNR for a given (up-/downlink) frequency."""
    if case_number == 1 or case_number == 2:
        SNR = P_T(frequency) + G_T(frequency) + L_TS + L_TG + L_P(frequency) + L_A(frequency) + L_FS(frequency) + G_R(frequency) - T_s(frequency) - R(frequency) - k_B  # Signal-to-noise ratio [dB]

    if case_number == 3 or case_number == 4:
        SNR = P_T(frequency) + G_T(frequency) + L_TS + L_TG + L_P(frequency) + L_A(frequency) + L_S(frequency) + G_R(frequency) - T_s(frequency) - R(frequency) - k_B  # Signal-to-noise ratio [dB]

    return SNR

SNR_required = 4.8  # Required signal-to-noise ratio [dB]
def SNR_margin(frequency):
    """Calculates the margin."""
    SNR_margin = SNR(frequency) - SNR_required  # Signal-to-noise ratio margin [dB] (must be larger than 3 dB)

    return SNR_margin

if case_number == 1 or case_number == 2:
    print(f"Name | Downlink | Uplink\n"
          f"P_T | {P_T(Spacecraft.freq_downlink)} | {P_T(Spacecraft.freq_uplink)}\n"
          f"G_T | {G_T(Spacecraft.freq_downlink)} | {G_T(Spacecraft.freq_uplink)}\n"
          f"L_TS | {L_TS} | {L_TS}\n"
          f"L_TG | {L_TG} | {L_TG}\n"
          f"L_P | {L_P(Spacecraft.freq_downlink)} | {L_P(Spacecraft.freq_uplink)}\n"
          f"L_A | {L_A(Spacecraft.freq_downlink)} | {L_A(Spacecraft.freq_uplink)}\n"
          f"L_FS | {L_FS(Spacecraft.freq_downlink)} | {L_FS(Spacecraft.freq_uplink)}\n"
          f"G_R | {G_R(Spacecraft.freq_downlink)} | {G_R(Spacecraft.freq_uplink)}\n"
          f"T_s | {T_s(Spacecraft.freq_downlink)} | {T_s(Spacecraft.freq_uplink)}\n"
          f"R | {R(Spacecraft.freq_downlink)} | {R(Spacecraft.freq_uplink)}\n"
          f"k_B | -228.6 | -228.6\n"
          f"SNR | {SNR(Spacecraft.freq_downlink)} | {SNR(Spacecraft.freq_uplink)}\n"
          f"SNR_required | {SNR_required} | {SNR_required}\n"
          f"SNR_margin | {SNR_margin(Spacecraft.freq_downlink)} | {SNR_margin(Spacecraft.freq_uplink)}")

elif case_number == 3 or case_number == 4:
    print(f"Name | Downlink | Uplink\n"
          f"P_T | {P_T(Spacecraft.freq_downlink)} | {P_T(Spacecraft.freq_uplink)}\n"
          f"G_T | {G_T(Spacecraft.freq_downlink)} | {G_T(Spacecraft.freq_uplink)}\n"
          f"L_TS | {L_TS} | {L_TS}\n"
          f"L_TG | {L_TG} | {L_TG}\n"
          f"L_P | {L_P(Spacecraft.freq_downlink)} | {L_P(Spacecraft.freq_uplink)}\n"
          f"L_A | {L_A(Spacecraft.freq_downlink)} | {L_A(Spacecraft.freq_uplink)}\n"
          f"L_S | {L_S(Spacecraft.freq_downlink)} | {L_S(Spacecraft.freq_uplink)}\n"
          f"G_R | {G_R(Spacecraft.freq_downlink)} | {G_R(Spacecraft.freq_uplink)}\n"
          f"T_s | {T_s(Spacecraft.freq_downlink)} | {T_s(Spacecraft.freq_uplink)}\n"
          f"R | {R(Spacecraft.freq_downlink)} | {R(Spacecraft.freq_uplink)}\n"
          f"k_B | -228.6 | -228.6\n"
          f"SNR | {SNR(Spacecraft.freq_downlink)} | {SNR(Spacecraft.freq_uplink)}\n"
          f"SNR_required | {SNR_required} | {SNR_required}\n"
          f"SNR_margin | {SNR_margin(Spacecraft.freq_downlink)} | {SNR_margin(Spacecraft.freq_uplink)}")