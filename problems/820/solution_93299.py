def posLetra(frase,letra,numero):
    """função que recebe uma letra e a sua ocorrência, e retorna em que posição da string ela está;
       str,str,int -> int"""
    acumulador = 0
    proximo = 0
    while acumulador < numero and proximo < len(frase):
        if frase[proximo] == letra:
            acumulador = acumulador + 1
        proximo = proximo + 1
    if acumulador == numero :
        return proximo -1
    elif acumulador< n:
        return -1