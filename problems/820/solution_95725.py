def posLetra(frase,l,n):
    """
       """
    posiçao = 0
    contador = 0
    while posiçao < len(frase):
        if frase(posiçao) == l:
            contador = contador + 1
            if contador = n:
                return contador