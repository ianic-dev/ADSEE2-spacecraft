import math as m


class Spacecraft:
    transmit_P = 50 # W
    transmit_loss_f = 0.8  # -              '''May be changed'''
    freq_downlink = 2.5  # GHz              '''May be changed'''
    #freq_downlink = freq_downlink/1e9  # to Hz
    turnaround_r = 221/240  # -
    freq_uplink = freq_downlink * turnaround_r  # GHz          '''May be changed'''
    antenna_d = 0.2  # m
    L_A0_up = 0.035
    L_A0_down = 0.036

class Payload:
    width_angle = 20  # deg
    width_angle = m.radians(width_angle)  # rad
    px_size = 0.1  # arcmin
    px_size = px_size/60  # deg
    px_size = m.radians(px_size)  # rad
    bit_depth = 8  # bit/px
    duty_cycle = 0.6  # -
    downlink_time_p_day = 3  # hr
    downlink_fraction = downlink_time_p_day/24  # -


class Requirement:
    uplink_data_rate = 1e8  # bit/s
    BER = 1e-6  # -


class Orbit:
    altitude = 500 # km                        '''May be changed'''
    altitude = altitude * 1000  # m
    elongation_angle = 0  # deg
    elongation_angle = m.radians(elongation_angle)  # rad
    pointing_offst = 0.1  # deg

    parent = "Earth"
    radius = 6371000 + altitude  # m
    grav_param = 3.986e14  # m^3/s^2
    period = 2*m.pi*m.sqrt(radius**3/grav_param)  # s


class Ground_station:
    transmit_P = 520  # W       '''May be changed'''
    antenna_d = 0.5  # m
    loss_factor = 0.7  #           '''May be changed'''
    T_s_down = 135  # K
    T_s_up = 614  # K


class ADCS:
    mmoi = 2.5  # kgm^2
    dist_torque = 1e-6  # Nm
    moment_arm = 0.2  # m
    manoevre_angle = 90  # deg
    manoevre_time = 10  # s
    manoevre_angle = m.radians(manoevre_angle)  # rad
    pointing_knowledge = 50  # arcsec
    pointing_knowledge = pointing_knowledge/3600  # deg
    pointing_knowledge = m.radians(pointing_knowledge)  # rad
