def posLetra(frase,letra,ocorrencia):
    """Recebe uma frase, uma letra e um número de ocorrência e devolve a posição em que essa letra se encontra"""
    indice=0
    numeroderepeticoes=0
    numerodeletras=str.count(frase,letra)
    if ocorrencia>numerodeletras:
        return -1
    while numeroderepeticoes<=ocorrencia:
        if frase[indice]==letra:
            numeroderepeticoes=numeroderepeticoes+1
        else:
            numeroderepeticoes=numeroderepticoes
        indice=indice+1
    return indice