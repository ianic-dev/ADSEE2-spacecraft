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
    width_angle = 20  # deg
    width_angle = m.radians(width_angle)  # rad
    px_size = 0.1  # arcmin
    px_size = px_size*60  # deg
    px_size = m.radians(px_size)  # rad
    bit_depth = 8  # bit/px
    duty_cycle = 0.6  # -
    downlink_time_p_day = 3  # hr
    downlink_fraction = downlink_time_p_day/24  # -


class Requirement:
    uplink_data_rate = 1e8  # bit/s
    BER = 1e-6  # -


class Orbit:
    altitude = 500  # km
    altitude = altitude * 1000  # m
    elongation_angle = "N/A"  # deg
    elongation_angle = m.radians(elongation_angle)  # rad
    pointing_offst = 0.1  # deg
    pointing_offst = m.radians(pointing_offst)  # rad

    parent = "Earth"
    radius = 6371000 + altitude  # m
    grav_param = 3.986e14  # m^3/s^2
    period = 2*m.pi*m.sqrt(radius**3/grav_param)  # s


class Ground_station:
    transmit_P = 400  # W
    antenna_d = 0.5  # m
    loss_factor = 0.7


class ACDS:
    mmoi = 2.5  # kgm^2
    dist_torque = 1e-6  # Nm
    moment_arm = 0.2  # m
    manoevre_angle = 90  # deg
    manoevre_time = 10  # s
    manoevre_angle = m.radians(manoevre_angle)  # rad
    pointing_knowledge = 50  # arcsec
    pointing_knowledge = pointing_knowledge/3600  # deg
    pointing_knowledge = m.radians(pointing_knowledge)  # rad
