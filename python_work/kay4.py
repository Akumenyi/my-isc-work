import serial #do ls -F /dev/serial/by-id/* in terminal

ser = serial.Serial(
    port='/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)

print ser.read(8)
ser.close()


from datetime import	datetime
import serial

ser = serial.Serial(
    port='/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)
while ser.isOpen():
    datastring	= ser.read(size=8)
    print datetime.utcnow().isoformat(),	datastring

#print	datetime.utcnow().isoformat(),	ser.read(size=8)


#rewriting above code to use readline()
from	datetime	import	datetime
import	serial,	io
ser = serial.Serial(
    port='/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0',
    baudrate=9600,)

sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser,1),encoding='ascii',newline='\r')

while	ser.isOpen():
    datastring=sio.readline()
    print datetime.utcnow().isoformat(), datastring
ser.close()

#writing output temp data to file
from datetime import datetime
import	serial,	io

outfile='/tmp/serial-temperature.tsv'

ser = serial.Serial(
    port='/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0',
    baudrate=9600,)

sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser,1),encoding='ascii',newline='\r')

with open(outfile,'a') as f: #appends to existing file
    while ser.isOpen():
    datastring=sio.readline()   #\t is tab; \n is line separator
    f.write(datetime.utcnow().isoformat() +	'\t' +	datastring + '\n')
    f.flush()	#included to force the system to write	to disk

ser.close()
