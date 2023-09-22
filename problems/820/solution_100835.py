def posLetra (string, letra, numero):
    pos = str.find(string, letra)
    pos_ant = pos
    event = 1 if not pos == -1 else 0
    incid = event
    while event and incid < incid_max:
        pos_ant = pos
        pos = str.find(string, letra, pos + 1, len(string) - 1)
        event = 1 if not pos == -1 else 0
        incid += event
    return incid,pos