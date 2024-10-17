import math
import numpy as np
from data import Spacecraft, Payload, Requirement, Orbit, Ground_station

k_B = -228.6  # dB

# transmitter performance
c = 3*10**8  # m/s
Lambda = c / Spacecraft.freq_downlink
radiation_efficiency = 1
antenna_gain = 10 * math.log(radiation_efficiency * (
    (4 * np.pi * (np.pi * Spacecraft.antenna_d**2 / 4))/Lambda**2), 10)  # dB
EIRP = 10 * math.log((Spacecraft.transmit_P / 1), 10) - \
    Spacecraft.transmit_loss_f + antenna_gain  # dB

# Free Space Loss
L_FS = 20 * math.log((4 * math.pi * 1)/Lambda)  # dB

# Space Loss
L_S = 1
# Atmospheric Loss
L_A = 3

# Payload data rate
image_width = math.arctan(Payload.width_angle / 2) * Orbit.altitude  # m
n_pixels_line = Payload.width_angle / Payload.px_size
pixel_width = image_width / n_pixels_line   # m
lines_per_second = v_orbit / pixel_width
generatd_data_rate = n_pixels_line * \
    lines_per_second * Payload.bit_depth   # bits/s

# Required Data Rate
B_r = generated_data_rate * (Payload.duty_cycle / Payload.downlink_fraction)

# SNR calculation
SNR_received = EIRP - L_FS - L_S + (G/T) - 10*math.log(k_B * S_r, 10)
SNR_required = EIRP - L_FS - L_X + (G/T) - 10*math.log(k_B * b_r, 10)
