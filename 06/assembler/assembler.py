#!/usr/bin/env python

import Parser as par
import Codes as c
import argparse
from check_table import check_table

arg_parser = argparse.ArgumentParser(description = "")

arg_parser.add_argument('filename',
                        help = 'name of file to use',
                        action = 'store'
                       )
args = arg_parser.parse_args()

p = par.Parser(args.filename)
codes = c.Codes()
new_filename = args.filename[:-4] + '.hack'

# Next available RAM address starts at 16 and increments every time a
# variable is written to RAM
ram_addr = 16
for i, line in enumerate(p.code):
    p.set_current_command(i)
    command_type = p.command_type()

    # Initialise values before relevant ones are set for
    # the command
    symbol = 'null'
    dest = 'null'
    comp = 'null'
    jump = 'null'

    if command_type == 'C_COMMAND':
        dest, comp, jump = p.c_instr_parts()
        
        # For a C-command, the first 3 bits are always 1
        instr_code = '111'
        dest_code = codes.dest(dest)
        comp_code = codes.comp(comp)
        jump_code = codes.jump(jump)

        machine_code = ('%s%s%s%s' % (instr_code, comp_code, dest_code, 
                                      jump_code))

        with open(new_filename, 'a') as hack:
            hack.write(machine_code + '\n')

    elif command_type == 'A_COMMAND':
        symbol = p.symbol()

        symbol_table = p.symbol_table
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # Convert symbols to addresses
        if p.symbol_table.contains(symbol):
            symbol = symbol_table.get_address(symbol)
        elif symbol[0] not in numbers:
            symbol_table.add_entry(symbol, ram_addr)
            
            symbol = ram_addr
            ram_addr += 1

        # Convert to 15 bit wide binary representation
        # 17 here because it includes the leading '0b'
        # which the slice then removes
        int_symbol = int(symbol)
        addr_code = "{0:017b}".format(int_symbol)[2:]
        instr_code = '0' 

        machine_code = instr_code + addr_code

        with open(new_filename, 'a') as hack:
            hack.write(machine_code + '\n')


