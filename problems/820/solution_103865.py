def posLetra(frase,letra,ocorrencia):
    if str.count(frase,letra)==ocorrencia:
        return str.index(frase,letra)
    else:
        return -1