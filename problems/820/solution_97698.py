def posLetra(string,letra,numero):
    posicao = str.find(string, letra)
    pos_anterior = posicao
    ocorrencia = 1 if not posicao == -1 else 0
    incid = ocorrencia
    while ocorrencia and incid < numero:
        
        posicao = str.find(string,letra, posicao + 1, len(string))
        incid += ocorrencia
    return (posicao)