def encontrar(cadeia, letter, incid_max):
    posicao = str.find(frase, letra)
    pos_anterior = posicao
    event = 1 if not pos == -1 else 0
    incid = event
    while event and incid < incid_max:
        pos_ant = pos
        pos = str.find(cadeia, letter, pos + 1, len(cadeia) - 1)
        event = 1 if not pos == -1 else 0
        incid += event
    return pos