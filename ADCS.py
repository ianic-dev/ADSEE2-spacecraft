from data import ACDS

req_torque = ACDS.mmoi*ACDS.manoevre_angle*4/(ACDS.manoevre_time)
print(req_torque)
