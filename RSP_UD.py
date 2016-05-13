'''
Checks if response from M-Bus command REQ_UD2 is OK.
Note: Input must be one long byte array with no spaces.

RSP_UD format:
68 L L 68 C ADR CI ID ID ID ID MAN MAN VER MED AN STA SIG SIG . . .  CS END
---Information----|---Header---------------------------------|-DATA-|------|

'''

import sys

if len(sys.argv) < 2:
	print("Error: Too few arguments.")
	sys.exit()
elif len(sys.argv) > 2:
	print("Error: Too many arguments.")
	sys.exit()

response = []	# Will hold the RSP_UD telegram.
	
# Iterate over every other characters.
for start in range(0, len(sys.argv[1]), 2):

	# Try to convert hex string to int.
	try:
		temp = int(sys.argv[1][start:start + 2], 16)
		response.append(temp)
	except:
		print("Error: '%s' contains a non hexadecimal number."%(sys.argv[1]))
		sys.exit()	
	
if len(response) < 21:
	print("Error: Too few bytes received.")
	sys.exit()
elif len(response) > 261:
	print("Error: Too many bytes received.")
	sys.exit()

length = len(response)

# Calculate checksum.
cs = 0
for b in response[4:length-2]:
	cs += b
cs = cs & 0xFF

# Check RSP_UD.
okInfo = response[0] == response[3] and response[1] == response[2]
okLength = (length - 6) == response[1]
okCS = cs == response[length-2]
okEnd = response[length-1] == 0x16

if okInfo and okLength and okCS and okEnd:
	print("RSP_UD OK")
else:
	print("RSP_UD NOK")
