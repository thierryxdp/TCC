def posLetra(frase,letra,numero):
    i = 0
    while i < (numero+1):
        if  numero<=str.count(frase,letra) and numero == 1:
                ocorrencia = str.index(frase,letra)
                return ocorrencia
        elif numero<=str.count(frase,letra):
            ocorrencia = str.index(frase,letra)
            retorno = str.index(frase,letra,ocorrencia + 1)
        else:
            return -1
        i = i + 1
    return retorno