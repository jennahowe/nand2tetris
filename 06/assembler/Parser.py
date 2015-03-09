"""Slice the string into sections which define different parts of the 
command.

instruct_code determines whether the command is an A-instruction or a 
C-instruction, 0 for an A-instruction, 1 for a C-instruction.

a_value contains the last 15 bits of the command, for an A-instruction these
are the binary representation of the value to be stored in the A 
register.

am_reg, for a C-instruction, this bit is zero if the command deals with
the A register, or 1 if it deals with the M register.

comp is the main section of the computation to be performed. It could
be something like 'A-1' or '1' or 'D-M'. The codes for 'A-D' and 'M-D' 
are the same apart from the value of am_reg, which determines whether 
to use the A register or the M register.

dest says which registers to store comp in. For example: 'A=-1', 
'MD=M+D'.

jump, says whether to execute something other than the next line in the 
program. It might say to jump back to an earlier line.

self.instruct_code = command[0]
self.a_value = command[1:15]
self.am_reg = command[3]
self.comp = command[4:9]
self.dest = command[10:12]
self.jump = command[13:15]
"""

class Parser:
    """A class to handle parsing each line of an assembly program"""
    def __init__(self, assembly_file):
        """Open filestream for assembly file and prepare to parse it."""
        with open(assembly_file, 'r') as raw_code:
            code = []
            for line in raw_code:
                # Strip whitespace
                line = line.strip('\n\r')
                line = line.replace(' ', '')
                line = line.replace('\t', '')

                # Remove comments
                split_comments = line.split('//')
                line = split_comments[0]

                # Empty lines or lines with just comments will now be of zero
                # length and will be ignored
                if len(line) > 0:
                    code.append(line)

            self.code = code






