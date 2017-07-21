# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MCP23008
# This code is designed to work with the MCP23008_I2CR8G5LE_10A I2C relay controller available from ControlEverything.com.
# https://shop.controleverything.com/collections/color/products/isl29125-digital-rgb-color-light-sensor-with-ir-blocking-filter
import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# ISL29125 address, 0x44(68)
# Select configuation-1register, 0x01(01)
#               0x0D(13)        Operation: RGB, Range: 10000 lux, Res: 16 Bits
bus.write_byte_data(0x44, 0x01, 0x0D)

time.sleep(0.5)
# ISL29125 address, 0x44(68)
# Read data back from 0x09(9), 6 bytes
# Green LSB, Green MSB, Red LSB, Red MSB, Blue LSB, Blue MSB
data = bus.read_i2c_block_data(0x44, 0x09, 6)

# Convert the data
green = data[1] * 256 + data[0]
red = data[3] * 256 + data[2]
blue = data[5] * 256 + data[4]

# Output data to the screen
print "Green Color luminance : %d lux" %green
print "Red Color luminance : %d lux" %red
print "Blue Color luminance : %d lux" %blue
