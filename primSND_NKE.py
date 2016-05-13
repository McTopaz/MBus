'''
Creates the M-Bus SND_NKE command based on the primary address as only parameter in.

Example:
0 = 10 40 00 40 16
1 = 10 40 01 41 16
10 = 10 40 0A 4A 16

'''

import sys

start = 0x10
c = 0x40
adr = int(sys.argv[1])
cs = (c + adr) & 0xFF
end = 0x16

print("%02X%02X%02X%02X%02X"%(start, c, adr, cs, end))
