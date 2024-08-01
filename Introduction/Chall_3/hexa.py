#!/usr/bin/env python3

# Le text encrypte a souvent des des bytes et pas du ASCII char
# L'hexadecimal (base 16) peut etre utilise pour representer des ASCII


# PROCESS : ASCII --> Ordinal Number "ord()" --> Hexadecimal Conversion


hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
result = bytes.fromhex(hex_string)

print(result)
