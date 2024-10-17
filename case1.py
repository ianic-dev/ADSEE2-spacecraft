import math as m


class Spacecraft:
    transmit_P = 200  # W
    transmit_loss_f = 0.8  # -
    freq_downlink = 2.2  # GHz
    freq_downlink = freq_downlink/1e9  # to Hz
    turnaround_r = 221/240  # -
    freq_uplink = freq_downlink/turnaround_r  # Hz
    antenna_d = 0.2  # m


class Payload:
    width_angle = 0  # deg
    width_angle = m.radians(width_angle)  # rad
    px_size = 0  # arcmin
    px_size = px_size*60  # deg
    px_size = m.radians(px_size)  # rad
    bit_depth = 0  # bit/px
    duty_cycle = 0  # -
    downlink_time_p_day = 0  # hr
    downlink_fraction = downlink_time_p_day/24  # -


class Requirement:
    uplink_data_rate = 0  # bit/s
    BER = 0  # -


class Orbit:
    altitude = 0  # km
    altitude = altitude * 1000  # m
    radius = altitude + 6371000  # m
    elongation_angle = 0  # deg
    elongation_angle = m.radians(elongation_angle)  # rad
    pointing_offst = 0  # deg
    pointing_offst = m.radians(pointing_offst)  # rad


class Ground_station:
    transmit_P = 0  # W
    antenna_d = 0  # m


class ACDS:
    mmoi = 0  # kgm^2
    dist_torque = 0  # Nm
    moment_arm = 0  # m
    manoevre_angle = 0  # deg
    manoevre_time = 0  # s
    manoevre_angle = m.radians(manoevre_angle)  # rad
    pointing_knowledge = 0  # arcsec
    pointing_knowledge = pointing_knowledge/3600  # deg
    pointing_knowledge = m.radians(pointing_knowledge)  # rad
