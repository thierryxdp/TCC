def posLetra (frase,letra,n):
    a = str.find(frase, letra)
    ocorrencia = 1
    if frase.count(letra)< n:
        return -1
    elif ocorrencia == n:
        return a
    else:
        while ocorrencia < n:
            x = str.find(frase,letra, a+1)
            a = x + 1
            ocorrencia = ocorrencia + 1
        return x