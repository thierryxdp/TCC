def posLetra(frase,letra,numero):
    i = 0
    while i < (numero+1):
        if  numero<=str.count(frase,letra):
            if numero == 1:
                ocorrencia = str.index(frase,letra)
                return ocorrencia
            else:
            ocorrencia = str.index(frase,letra)
            retorno = str.index(frase,letra,ocorrencia + 1)
        i = i + 1
    return retorno