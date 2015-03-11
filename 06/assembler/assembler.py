#!/usr/bin/env python
import Parser as par
import Codes as c
import argparse

arg_parser= argparse.ArgumentParser(description = "")

arg_parser.add_argument('filepath',
                    help = 'name of file to use',
                    action = 'store'
                   )
args = arg_parser.parse_args()

p = par.Parser(args.filepath)
codes = c.Codes()
new_filepath = args.filepath[:-4] + '.hack'

for i, line in enumerate(p.code):
    p.set_current_command(i)
    command_type = p.command_type()

    # initialise values before relevant ones are set for
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

        with open(new_filepath, 'a') as hack:
            hack.write(machine_code + '\n')

    elif command_type == 'L_COMMAND' or command_type == 'A_COMMAND':
        symbol = p.symbol()

        # Convert to 15 bit wide binary representation
        # Don't know why you have to put 17 to get the correct width?
        # The slice removes the leading '0b'
        int_symbol = int(symbol)
        symbol_code = "{0:017b}".format(int_symbol)[2:]
        instr_code = '0' 

        machine_code = instr_code + symbol_code

        with open(new_filepath, 'a') as hack:
            hack.write(machine_code + '\n')
    else:
        print('If this prints then something weird is happening')


