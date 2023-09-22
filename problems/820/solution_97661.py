def posLetra(cadeia, letter, incid_max):
    pos = str.find(cadeia, letter)
    pos_ant = pos
    event = 1 if not pos == -1 else 0
    #incid = 1 if not pos == -1 else 0
    incid = event
    #if pos + 1:
    #while pos + 1:
    while event and incid < incid_max:
        pos_ant = pos
        pos = str.find(cadeia, letter, pos + 1, len(cadeia) - 1)
        event = 1 if not pos == -1 else 0
        #incid += 1 if not pos == -1 else 0
        incid += event
    return pos