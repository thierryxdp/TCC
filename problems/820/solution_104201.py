def posLetra(frase,letra,ocorrencia)    
    lista = frase.split()
    posicao = []
    x = 1 
    for i in range(len(lista)):
        if lista[i] == letra:
            posicao.append(i)
    return posicao[ocorrencia]