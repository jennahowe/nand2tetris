class Codes:
    """Translates Hack assembly language mnemonics in binary code."""
    def __init__(self):
        self.dest_codes = {'null': '000',
                           'M': '001',
                           'D': '010',
                           'MD': '011',
                           'A': '100',
                           'AM': '101',
                           'AD': '110',
                           'AMD': '111'
                          }
        self.comp_codes = {'0': '0101010',
                           '1': '0111111',
                           '-1': '0111010',
                           'D': '0001100',
                           'A': '0110000',
                           '!D': '0001101',
                           '!A': '0110011',
                           '-D': '0001111',
                           '-A': '0110011',
                           'D+1': '0011111',
                           'A+1': '0110111',
                           'D-1': '0001110',
                           'A-1': '0110010',
                           'D+A': '0000010',
                           'D-A': '0010011',
                           'A-D': '0000111',
                           'D&A': '0000000',
                           'D|A': '0010101',
                           'M': '1110000',
                           '!M': '1110011',
                           '-M': '1110011',
                           'M+1': '1110111',
                           'M-1': '1110010',
                           'D+M': '1000010',
                           'D-M': '1010011',
                           'M-D': '1000111',
                           'D&M': '1000000',
                           'D|M': '1010101'
                           }
        self.jump_codes = {'null': '000',
                           'JGT': '001',
                           'JEQ': '010',
                           'JGE': '011',
                           'JLT': '100',
                           'JNE': '101',
                           'JLE': '110',
                           'JMP': '111'
                          }

    def dest(self, mnemonic):
        dest_code = self.dest_codes[mnemonic]
        return dest_code
    def comp(self, mnemonic):
        comp_code = self.comp_codes[mnemonic]
        return comp_code
    def jump(self, mnemonic):
        jump_code = self.jump_codes[mnemonic]
        return jump_code
