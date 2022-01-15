#!/usr/bin/python3

import serial

serport = '/dev/ttyUSB0'
baud = '9600'

channelspace = '0'      # 0=12.5kHz, 1=25kHz

#rxfreq = '430.7875'
#txfreq = '438.3875'

rxfreq = '438.3875'
txfreq = '430.7875'
#rxfreq = '144.9000'     # TX frequency
#txfreq = rxfreq         # Same as rx freq.

squelch = '1'           # 0-8 (0 = open)

txcxcss = '0000'        # CTCSS / CDCSS
rxcxcss = txcxcss       # CTCSS / CDCSS


ser = serial.Serial(serport, baud, timeout=2)
print('Opening port: ' + ser.name) 

print ('\r\nConnecting...')
ser.write(b'AT+DMOCONNECT\r\n')

output = ser.readline()
print ('reply: ' + output.decode("utf-8"))

print ('\r\nConfiguring radio...')
config = 'AT+DMOSETGROUP={},{},{},{},{},{}\r\n'.format(channelspace, txfreq, rxfreq, txcxcss, squelch, rxcxcss)
ser.write(config.encode())
output = ser.readline()
print ('reply: ' + output.decode("utf-8"))

print ('\r\nDisabling filters...')
ser.write(b'AT+SETFILTER=0,0,0\r\n')
output = ser.readline()
print ('reply: ' + output.decode("utf-8"))

print ('\r\nSetting volume...')
ser.write(b'AT+DMOSETVOLUME=5\r\n')
output = ser.readline()
print ('reply: ' + output.decode("utf-8"))

