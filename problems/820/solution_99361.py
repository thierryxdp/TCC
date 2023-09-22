def posLetra(frase,letra,ocorrencia):
    i=0
    retorno=() 
    while i < len(frase):
        if letra==frase[i]: 
            retorno=(i,)
        i=i+1
    return retorno[ocorrencia-1]