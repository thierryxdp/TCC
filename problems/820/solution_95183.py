def posLetra(string,letra,ocorrencia):
    quantidadeletras = str.count(string,letra)
    contador = 1
    if quantidadeletras < ocorrência:
        return -1
    else:
        while contador <= ocorrência:
            a = str.index(string,letra)
            contador = contador + 1
    return a