def posLetra(frase,letra,n):
    tamanho=len(frase)
    indice=0
    achei=False
    retorno=-1
    contador=0
    while indice < tamanho or not achei:
        if frase[indice]==letra:
            contador+=1
        if contador==n:
            retorno=indice
            achei=True
        indice+=1
    return retorno