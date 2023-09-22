def posLetra(string,letra,numero):
    posicao = str.find(string, letra)
    pos_anterior = posicao
    event = 1 if not posicao == -1 else 0
    
    while event and incid < numero:
        pos_anterior = posicao
        posicao = str.find(string,letra, posicao + 1, len(string))
        event = 1 if not posicao == -1 else 0
        
    return (posicao)