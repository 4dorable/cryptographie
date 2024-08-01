#!/usr/bin/env python3
import base64

# Encoding courrant--> base64
# permet de representeDonnes binaire en ASCII String de 64 char

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes_string = bytes.fromhex(hex_string)
result = base64.b64encode(bytes_string)

print(result)
