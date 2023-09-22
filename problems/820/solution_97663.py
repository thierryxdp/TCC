def posLetra(cadeia, letter, incid_max):
    pos = str.find(cadeia, letter)
    pos_ant = pos
    event = 1 if not pos == -1 else 0
    incid = event
   
    return pos