def posLetra(frase,letra,posiçao):
    """calculo e retorno de uma funçao que retorne em que posiçao da string a ocorrencia da letra esta."""
    i= frase.find(letra)
    while i >= 0 and posiçao > 1:
        i= frase.find(letra,i+ 1)
        posiçao =posiçao+1
    return i