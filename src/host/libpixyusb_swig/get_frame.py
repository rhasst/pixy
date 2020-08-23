from pixy import *

# Pixy Python SWIG get frame example #

print ("Pixy Python SWIG Example -- Get Blocks")

# Initialize Pixy Interpreter thread #
pixy_init()

framePtr = FramePtr()
response = pixy_get_frame(framePtr)

frame = framePtr.cast()
print(frame.response)
print(frame.fourccc)
print(frame.renderflags)
print(frame.xwidth)
print(frame.ywidth)
print(frame.size)