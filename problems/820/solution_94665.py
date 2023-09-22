def posLetra(frase, letra, ocorrencia):
    cont = 0
    i = 0
    while i<len(frase):
        if frase[i] == letra:
            cont = cont +1
            if cont = ocorrencia:
                resposta = i
    if cont<ocorrencia:
        resposta = -1
        
    return resposta