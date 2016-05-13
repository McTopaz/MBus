'''
Checks if response from M-Bus commands SND_NKE, APP_RST, SND_UD and SLV_SEL is 0x16.
Note: Input must be 'E5'.
'''

import sys

if len(sys.argv) < 2:
	print("Error: Too few arguments.")
	sys.exit()
elif len(sys.argv) > 2:
	print("Error: Too many arguments.")
	sys.exit()

value = 0
	
try:
	value = int(sys.argv[1], 16)
except:
	print("Error: Unknown input [%s]"%(sys.argv[1]))
	sys.exit()

if value == 0xE5:
	print("[ACK] 0x%02X"%(value))
else:
	print("Error: Unknown value [0x%02X]"%(value))
