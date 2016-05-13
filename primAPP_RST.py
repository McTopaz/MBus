'''
Creates the M-Bus APP_RST command based on the primary address as only parameter in.
Note: The C field is set to 0x7B.

APP_RST format:
68 L L 68 C ADR CI CS 16
'''

import sys

start = 0x68
L = 0x3
c = 0x53
adr = int(sys.argv[1])
ci = 0x50
cs = (c + adr + ci) & 0xFF
end = 0x16

print("%02X%02X%02X%02X%02X%02X%02X%02X%02X"%(start, L, L, start, c, adr, ci, cs, end))
