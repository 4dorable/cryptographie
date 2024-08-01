#!/usr/bin/env python3

int_array = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
chr_array = []
# La fonction chr() converti ASCII Number --> character
# La fonction ord() character --> ASCII number

for number in int_array:
    chr_array.append(chr(number))


result = "".join(chr_array)
print(result)
