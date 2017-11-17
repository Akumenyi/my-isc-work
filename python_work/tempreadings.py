#writing output temp data to file
from datetime import datetime
import	serial,	io
import time

abort_after = 5 * 60
start = time.time()
endtime = start + abort_after

outfile='/tmp/serial-temperature.tsv'

ser = serial.Serial(
    port='/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0',
    baudrate=9600,)

sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser,1),encoding='ascii',newline='\r')

with open(outfile,'a') as f: #appends to existing file
    while ser.isOpen() and time.time() < endtime:
        datastring = sio.readline()   #\t is tab; \n is line separator
        f.write(datetime.utcnow().isoformat() +	'\t' +	datastring + '\n')
        f.flush()	#included to force the system to write	to disk
        
ser.close()
