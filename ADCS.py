from case4 import ADCS, Orbit
import math as m

req_torque = ADCS.mmoi*ADCS.manoevre_angle*4/(ADCS.manoevre_time)
req_momentum = (m.sqrt(2)/2) * ADCS.dist_torque * Orbit.period/4
print(req_torque)
