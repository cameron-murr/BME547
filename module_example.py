from blood_calculator import *
import math

print("This is the databse module and python calls it {}".format(__name__))

HDL_value = 55

classification = check_HDL(HDL_value)
print("{} is {}".format(HDL_value, classification))
x = check_LDL(200)
print(x)
