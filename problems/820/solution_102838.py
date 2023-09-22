def posLetra(frase,letra,ocorrencia):
    """Recebe uma frase, uma letra e um número de ocorrência e devolve a posição em que essa letra se encontra;
    	str, str, int -> int"""
    indice=0
    numeroderepeticoes=0
    numerodeletras=str.count(frase,letra)
    if ocorrencia>numerodeletras:
        return -1
    while numeroderepeticoes<ocorrencia:
        letradafrase=frase[indice]
        if letradafrase==letra:
            numeroderepeticoes=numeroderepeticoes+1
        indice=indice+1
    return indice