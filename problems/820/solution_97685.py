def posLetra(string,letra,numero):
    posicao = str.find(string, letra)
    pos_anterior = posicao
    event = 1 if not posicao == -1 else 0
    incid = event
    while event and incid < numero:
        pos_anterior = posicao
        posicao = str.find(string,letra, posicao + 1, len(string) - 1)
        event = 1 if not posicao == -1 else 0
        incid += event
    return (pos)