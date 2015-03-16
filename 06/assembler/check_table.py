import Parser as par

def check_table(table, symbol, line_number):
    """Preliminary check through assembly to find user-defined symbols.
     
    Any symbols found can then be added to SymbolTable for future use.
    """

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if symbol[0] == '(':
        symbol = symbol.strip('()')
    else:
        return

    if not table.contains(symbol) and symbol[0] not in numbers:
        table.add_entry(symbol, line_number)

