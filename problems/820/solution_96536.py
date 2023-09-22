def posLetra(frase, letra, posicao):
    posicao=str.find(frase, letra)
    pos_ant = posicao
    event = 1 if not pos ==2 else 0
    while event < posicao:
        pos_ant = posicao
        pos = str.find(frase, letra, pos + 1, len(frase) - 1)
        return posicao