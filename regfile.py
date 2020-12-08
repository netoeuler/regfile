#regfile
#Author: netoeuler

from datetime import datetime

regfile = open('SYSTEM','rb')

#BASE BLOCK
base_block = regfile.read(4096)

if base_block[0:4].decode('utf-8') != 'regf':
	die('Wrong magic number')

field_value = ''
for i in range(7,3,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Primary sequence number: '+str(int('0x'+field_value,0)))

field_value = ''
for i in range(11,7,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Secondary sequence number: '+str(int('0x'+field_value,0)))

field_value = ''
for i in range(19,11,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Last written timestamp: '+str(int('0x'+field_value,0)))
#print('Last written timestamp: '+str(datetime.fromtimestamp(int('0x'+field_value,0))))

field_value = ''
for i in range(23,19,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Major version: '+str(int('0x'+field_value,0)))

field_value = ''
for i in range(27,23,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Minor version: '+str(int('0x'+field_value,0)))

field_value = ''
for i in range(31,27,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('File type: '+str(int('0x'+field_value,0)))

field_value = ''
for i in range(35,31,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('File format: '+str(int('0x'+field_value,0)))

field_value = ''
for i in range(39,35,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Root cell offset: '+str(int('0x'+field_value,0)))

field_value = ''
for i in range(43,39,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Hive bins data size: '+str(int('0x'+field_value,0)))

field_value = ''
for i in range(47,43,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Clustering factor: '+str(int('0x'+field_value,0)))

print('Filename: '+base_block[48:112].decode('utf-16'))

field_value = ''
for i in range(511,507,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Checksum: '+str(int('0x'+field_value,0)))

field_value = ''
for i in range(4091,4087,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Boot type: '+str(int('0x'+field_value,0)))

field_value = ''
for i in range(4095,4091,-1):
	field_value+= str(hex(base_block[i])).replace('0x','')
print('Boot recover: '+str(int('0x'+field_value,0)))