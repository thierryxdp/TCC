def posLetra(string,letra,numero):
    posicao = str.find(string, letra)
    pos_anterior = posicao
    
    incid = ocorrencia
    while ocorrencia and incid < numero:
        posicao = str.find(string,letra, posicao + 1, len(string))
        incid += ocorrencia
    return (posicao)