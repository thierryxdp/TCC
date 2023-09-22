def posLetra(frase,letra,ocorrencia):
    indice=0
    while indice<len(frase):
        if frase[indice]==letra:
            tupla=tupla+(frase[indice],)
        indice=indice+1
    return