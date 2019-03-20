from pixy import *
from ctypes import *

# Pixy Python SWIG get blocks example #

print ("Pixy Python SWIG Example -- Pan Tilt")

# Initialize Pixy Interpreter thread #
pixy_init()

pixy_rcs_set_position(0, 450)
val = pixy_rcs_get_position(0)
print(val)