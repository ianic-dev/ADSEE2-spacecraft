import math as m


class SC:
    transmit_P = 0  # W
    transmit_loss_f = 0  # -
    freq_downlink = 0  # GHz
    freq_downlink = freq_downlink/1e9  # to Hz
    turnaround_r = 0  # -
    freq_uplink = freq_downlink/turnaround_r  # Hz
    antenna_d = 0  # m


class PL:
    width_angle = 0  # deg
    width_angle = m.radians(width_angle)  # rad
    px_size = 0  # arcmin
    px_size = px_size*60  # deg
    px_size = m.radians(px_size)  # rad
    bit_depth = 0  # bit/px
    duty_cycle = 0  # -
    downlink_time_p_day = 0  # hr
    downlink_fraction = downlink_time_p_day/24  # -


class Req:
    uplink_data_rate = 0  # bit/s
    BER = 0  # -


class Orbit:
    altitude = 0  # km
    altitude = altitude * 1000  # m
    radius = altitude + 6371000  # m
    elongation_angle = 0  # deg
    elongation_angle = m.radians(elongation_angle)  # rad
    pointing_offst = 0  # deg
    pointing_offst = m.radians(elongation_angle)  # rad


class GroundSt:
    transmit_P = 0  # W
    antenna_d = 0  # m
