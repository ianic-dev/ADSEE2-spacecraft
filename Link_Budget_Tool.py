import math
import numpy as np
from data.py import Spacecraft, Payload, Requirement, Orbit, Ground_station

#transmitter performance
c = 3*10**8 #m/s
Lambda = c / Spacecraft.freq_downlink
radiation_efficiency =
anntenna_gain = radiation_efficiency * ((4 * np.pi * (np.pi * Spacecraft.antenna_d**2 / 4))/Lambda**2)
EIRP = Spacecraft.transmit_P * Spacecraft.transmit_loss_f * f
