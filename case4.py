import math as m


class Spacecraft:
    transmit_P = 200  # W                              '''May be changed'''
    transmit_loss_f = 0.8  # -                          '''May be changed'''
    freq_downlink = 8.4  # GHz
    #freq_downlink = freq_downlink/1e9  # to Hz
    turnaround_r = 749/880  # -
    freq_uplink = freq_downlink * turnaround_r  # GHz
    antenna_d = 1  # m
    L_A0_up = 0.044
    L_A0_down = 0.046

class Payload:
    width_angle = 10  # deg                                     '''May be changed'''
    width_angle = m.radians(width_angle)  # rad
    px_size = 0.05  # arcmin
    px_size = px_size/60  # deg                                 '''May be changed'''
    px_size = m.radians(px_size)  # rad
    bit_depth = 8  # bit/px
    duty_cycle = 0.4  # -                                       '''May be changed'''
    downlink_time_p_day = 18  # hr                              '''May be changed'''
    downlink_fraction = downlink_time_p_day/24  # -


class Requirement:
    uplink_data_rate = 1e5  # bit/s
    BER = 1e-6  # -


class Orbit:
    altitude = 500  # km                                        '''May be changed'''
    altitude = altitude * 1000  # m
    elongation_angle = 10  # deg
    elongation_angle = m.radians(elongation_angle)  # rad
    pointing_offst = 0.05  # deg                                '''May be changed'''
    #pointing_offst = m.radians(pointing_offst)  # rad

    parent = "Mercury"
    orbit_radius = 58000000  # km
    radius = 2440500 + altitude  # m
    grav_param = 0.022032e15  # m^3/s^2
    period = 2*m.pi*m.sqrt(radius**3/grav_param)  # s


class Ground_station:
    transmit_P = 1400  # W                                      '''May be changed'''
    antenna_d = 35  # m
    loss_factor = 0.7                                           #'''May be changed'''
    T_s_down = 135  # K
    T_s_up = 614  # K


class ADCS:
    mmoi = 850  # kgm^2
    dist_torque = 1e-3  # Nm
    moment_arm = 1  # m
    manoevre_angle = 90  # deg
    manoevre_time = 30  # s
    manoevre_angle = m.radians(manoevre_angle)  # rad
    pointing_knowledge = 5  # arcsec
    pointing_knowledge = pointing_knowledge/3600  # deg
    pointing_knowledge = m.radians(pointing_knowledge)  # rad
