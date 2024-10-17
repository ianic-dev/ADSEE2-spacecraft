import math as m


class Spacecraft:
    transmit_P = 750  # W
    transmit_loss_f = 0.8  # -
    freq_downlink = 8.4  # GHz
    freq_downlink = freq_downlink/1e9  # to Hz
    turnaround_r = 749/880  # -
    freq_uplink = freq_downlink/turnaround_r  # Hz
    antenna_d = 2  # m
    L_A0_up = 0.05
    L_A0_down = 0.049

class Payload:
    width_angle = 10  # deg
    width_angle = m.radians(width_angle)  # rad
    px_size = 0.05  # arcmin
    px_size = px_size*60  # deg
    px_size = m.radians(px_size)  # rad
    bit_depth = 8  # bit/px
    duty_cycle = 0.15  # -
    downlink_time_p_day = 12  # hr
    downlink_fraction = downlink_time_p_day/24  # -


class Requirement:
    uplink_data_rate = 1e6  # bit/s
    BER = 1e-6  # -


class Orbit:
    altitude = 400  # km
    altitude = altitude * 1000  # m
    elongation_angle = 20  # deg
    elongation_angle = m.radians(elongation_angle)  # rad
    pointing_offst = 0.1  # deg
    pointing_offst = m.radians(pointing_offst)  # rad
    orbit_radius = 227900000 # km

    parent = "Mars"
    radius = 3396200 + altitude  # m
    grav_param = 0.042828e15  # m^3/s^2
    period = 2*m.pi*m.sqrt(radius**3/grav_param)  # s


class Ground_station:
    transmit_P = 1000  # W
    antenna_d = 35  # m
    loss_factor = 0.7
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
