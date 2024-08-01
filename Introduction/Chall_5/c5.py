#!/usr/bin/env python3

from Crypto.Util.number import *

# Systeme de crypto fonctionnent sur des nombres masi les messages bah c'est des lettres en gros
# Comment cvonvertir un message en suite de nombre pour faire des operations dessu ??


# message: HELLO
# ascii bytes: [72, 69, 76, 76, 79]
# hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
# base-16: 0x48454c4c4f
# base-10: 310400273487



base_10 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
base_16 = long_to_bytes(base_10)
print(base_16)
