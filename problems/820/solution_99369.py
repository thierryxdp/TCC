def posLetra(frase,letra,ocorrencia):
    i=0
    retorno=()
    numero=str.index(frase,letra)
    while i < len(frase):
        for letra in frase[i]: 
            retorno=(i,)
        i=i+1
    if numero<=ocorrencia:
        resposta=retorno[ocorrencia-1]
    else:
        if numero>ocorrencia:
            resposta= (-1) 
    return resposta