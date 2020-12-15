#regfile
#Author: netoeuler

from datetime import datetime

def calculate_checksum(D):
	C = 0

	G = []
	begin = 0
	end = 32
	for d in D:
		G.append(D[begin:end])
		begin += 32
		end += 32

	for g in G:
		g = int.from_bytes(g, "little")
		#print(type(C),type(g))
		C = C ^ g
		if C == -1:
			C = -2
		elif C == 0:
			C = 1

	return C

regfile = open('SYSTEM','rb')

#BASE BLOCK
base_block = regfile.read(4096)

if base_block[0:4].decode('utf-8') != 'regf':
	print('Wrong magic number')
	quit()

#Array with elements that contains [field_name, offset, length]
field_array = [['Primary sequence number',4,4], ['Secondary sequence number',8,4], ['Last written timestamp',12,8], 
	['Major version',20,4], ['Minor version',24,4], ['File type',28,4], ['File format',32,4], ['Root cell offset',36,4],
	['Hive bins data size',40,4], ['Clustering factor',44,4], ['Filename',48,64], ['Checksum',508,4], ['Boot type',4088,4],
	['Boot recover',4092,4]]
field_array = []

for f in field_array:
	field_name = f[0]
	offset = f[1]
	length = f[2]

	if field_name == 'Filename':
		print('Filename: '+base_block[48:112].decode('utf-16'))
		continue

	field_value = ''
	print(offset+length-1, str(offset-1))
	for i in range(offset+length-1, offset-1, -1):
		field_value+= str(hex(base_block[i])).replace('0x','')
	print(field_name+': '+str(int('0x'+field_value,0)))

print('Checksum: '+str(calculate_checksum(base_block[:508])))