import math as m


class Spacecraft:
    transmit_P = 200  # W
    transmit_loss_f = 0.8  # -                  '''May be changed'''
    freq_downlink = 2.2  # GHz                  '''May be changed'''
    #freq_downlink = freq_downlink/1e9  # to Hz
    turnaround_r = 221/240  # -
    freq_uplink = freq_downlink * turnaround_r  # GHz
    antenna_d = 4.2  # m
    L_A0_up = 0.035
    L_A0_down = 0.036


class Payload:
    width_angle = 45  # deg
    width_angle = m.radians(width_angle)  # rad
    px_size = 0.1  # arcmin
    px_size = px_size/60  # deg
    px_size = m.radians(px_size)  # rad
    bit_depth = 8  # bit/px
    duty_cycle = 0.8  # -                   '''May be changed'''
    downlink_time_p_day = 4  # hr
    downlink_fraction = downlink_time_p_day/24  # -


class Requirement:
    uplink_data_rate = 1e7  # bit/s
    BER = 1e-6  # -


class Orbit:
    altitude = 100  # km
    altitude = altitude * 1000 # m
    elongation_angle = "N/A"  # deg
    # elongation_angle = m.radians(elongation_angle)  # rad
    pointing_offst = 0.1  # deg                                 '''May be changed'''
    pointing_offst = m.radians(pointing_offst)  # rad

    parent = "Moon"
    radius = 1738100 + altitude  # m
    grav_param = 0.0049e15  # m^3/s^2
    period = 2*m.pi*m.sqrt(radius**3/grav_param)  # s


class Ground_station:
    transmit_P = 400  # W       '''May be changed'''
    antenna_d = 5  # m          '''May be changed'''
    loss_factor = 0.7           #'''May be changed'''
    T_s_down = 135  # K
    T_s_up = 614  # K


class ADCS:
    mmoi = 100  # kgm^2
    dist_torque = 1e-4  # Nm
    moment_arm = 1  # m
    manoevre_angle = 45  # deg
    manoevre_time = 60  # s
    manoevre_angle = m.radians(manoevre_angle)  # rad
    pointing_knowledge = 5  # arcsec
    pointing_knowledge = pointing_knowledge/3600  # deg
    pointing_knowledge = m.radians(pointing_knowledge)  # rad
