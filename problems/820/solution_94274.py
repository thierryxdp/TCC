def posLetra(frase,letra,posiçao):
    """calculo e retorno de uma funçao que retorne em que posiçao da string a ocorrencia da letra esta."""
    k= frase.find(letra)
    i=k
    while i >= 0 and posiçao > 1:
        i= k+1
        posiçao -= 1
    return i