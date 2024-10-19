import math as m


class Spacecraft:
    transmit_P = 50  # W                           '''May be changed'''
    transmit_loss_f = 0.8  # -                      '''May be changed'''
    freq_downlink = 8.4  # GHz
    #freq_downlink = freq_downlink/1e9  # to Hz
    turnaround_r = 749/880  # -
    freq_uplink = freq_downlink * turnaround_r  # GHz
    antenna_d = 2  # m
    L_A0_up = 0.044
    L_A0_down = 0.046

class Payload:
    width_angle = 10  # deg                         '''May be changed'''
    width_angle = m.radians(width_angle)  # rad
    px_size = 0.05  # arcmin
    px_size = px_size/60  # deg
    px_size = m.radians(px_size)  # rad
    bit_depth = 8  # bit/px
    duty_cycle = 0.15  # -
    downlink_time_p_day = 12  # hr
    downlink_fraction = downlink_time_p_day/24  # -


class Requirement:
    uplink_data_rate = 1e6  # bit/s
    BER = 1e-6  # -


class Orbit:
    altitude = 400  # km                    '''May be changed'''
    altitude = altitude * 1000  # m
    elongation_angle = 20  # deg
    elongation_angle = m.radians(elongation_angle)  # rad
    pointing_offst = 0.1  # deg                                 '''May be changed'''
    #pointing_offst = m.radians(pointing_offst)  # rad

    parent = "Mars"
    orbit_radius = 227900000 # km
    radius = 3396200 + altitude  # m
    grav_param = 0.042828e15  # m^3/s^2
    period = 2*m.pi*m.sqrt(radius**3/grav_param)  # s


class Ground_station:
    transmit_P = 2000  # W
    antenna_d = 50  # m             '''May be changed'''
    loss_factor = 0.7               #'''May be changed'''
    T_s_down = 135  # K
    T_s_up = 614  # K


class ADCS:
    mmoi = 100  # kgm^2
    dist_torque = 1e-2  # Nm
    moment_arm = 1  # m
    manoevre_angle = 30  # deg
    manoevre_time = 30  # s
    manoevre_angle = m.radians(manoevre_angle)  # rad
    pointing_knowledge = 50  # arcsec
    pointing_knowledge = pointing_knowledge/3600  # deg
    pointing_knowledge = m.radians(pointing_knowledge)  # rad
