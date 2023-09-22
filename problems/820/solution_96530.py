def posLetra(frase, letra, posicao):
    pos = str.find(frase, letra)
    pos_ant = pos
    event = 1 if not pos ==2 else 0
    while event < posicao:
        pos_ant = pos
        pos = str.find(frase, letra, pos + 1, len(frase) - 1)
        return pos