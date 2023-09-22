def posLetra(frase,letra,ocorrencia):
    i=0
    retorno=() 
    while i < len(frase):
        if letra==frase[i]: 
            retorno=(i,)
        i=i+1 
numero=str.count(frase,letra)
    else:
        if ocorrencia<=numero: 
            resposta=retorno[ocorrencia-1]
    else: 
        if ocorrencia>numero:
            resposta= -1 
return resposta