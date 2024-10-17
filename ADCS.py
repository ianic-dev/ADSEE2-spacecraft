from case4 import ADCS, Orbit
import math as m

req_torque = ADCS.mmoi*ADCS.manoevre_angle*4/(ADCS.manoevre_time**2)
req_momentum = (m.sqrt(2)/2) * ADCS.dist_torque * Orbit.period/4
print(req_torque)
print(req_torque, "is the required torque")
req_thrust = req_torque*0.5/ADCS.moment_arm
print(req_thrust, "is the required thrust")
