#!/usr/bin/python3

import urllib.request, json
import subprocess
import smbus
import time
import json

AM2320_ADDR = 0x5c
i2c = smbus.SMBus( 1 )

try:
	i2c.write_i2c_block_data( AM2320_ADDR ,0x00, [] )
except:
	pass

time.sleep(0.003)
i2c.write_i2c_block_data( AM2320_ADDR, 0x03, [ 0x00, 0x04 ] )

time.sleep(0.015)
data = i2c.read_i2c_block_data( AM2320_ADDR, 0x00, 6 )
humi = float( data[2] << 8 | data[3] ) / 10
room_temp = float( data[4] << 8 | data[5] ) / 10

list_data = {"TEMP":room_temp,"HUMI":humi}
data_json = json.dumps(list_data)

print(data_json)

#json_data = {"TEMP":room_temp,"HUMI":humi}
#json_data = {'TEMP':room_temp,'HUMI':humi}

#print(json_data.replace('\n',''))
#print(room_temp, humi)
#print(room_temp, humi)
#print(room_temp,'C')
#print(humi,'%')
