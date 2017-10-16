'''
This is a decode python use to decode virtual key code 
from string type hex code to integer in json file.
'''

import os, re

file_in = open(__file__+'/../virtual_key_hex_code.json', 'r')
file_out = open(__file__+'/../virtual_key_code.json','w')

for line in file_in.readlines():
    is_head = re.search('{', line)
    is_foot = re.search('}', line)
    if is_head == None and is_foot == None:
        hexCode = line.split(': ')[-1].strip(',\n')
        integer = int(hexCode.strip('"'),16)
        not_end = re.search(',', line)
        if not_end != None:
            line = line.split(': ')[0]+": "+str(integer)+",\n"
        else:
            line = line.split(': ')[0]+": "+str(integer)+"\n"
    file_out.write(line)