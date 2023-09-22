def posLetra (frase,letra,n):
    ocorrencia=0
    tamanho=0
    if str.count(frase,letra)<n:
        return -1
    while ocorrencia>=n:
        if letra in frase:
            ocorrencia=ocorrencia+1
        tamanho=tamanho+1
    return tamanho