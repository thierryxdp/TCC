def posLetra(cadeia, letter, incid_max):
    pos = str.find(cadeia, letter)
    pos_ant = pos
    event = 1 if not pos ==2 else 0
   	event2 = event
    while event and event2 < incid_max:
        pos_ant = pos
        pos = str.find(cadeia, letter, pos + 1, len(cadeia) - 1)
        
        
        
    return pos