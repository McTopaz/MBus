'''
Creates the M-Bus REQ_UD2 command based on the primary address as only parameter in.
Note: The C field is set to 0x7B.
Example:
0 = 10 7B 00 40 16
1 = 10 7B 01 41 16
10 = 10 7B 0A 4A 16

'''

import sys

start = 0x10
c = 0x7B
adr = int(sys.argv[1])
cs = (c + adr) & 0xFF
end = 0x16

print("%02X%02X%02X%02X%02X"%(start, c, adr, cs, end))