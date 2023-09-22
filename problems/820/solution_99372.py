def posLetra(frase,letra,ocorrencia):
    i=0
    retorno=[]
    numero=str.count(frase,letra)
    while i < len(frase):
        if letra in frase[i]: 
            list.append(retorno,i)
        i=i+1
    if numero<=ocorrencia:
        resposta=retorno[ocorrencia-1]
    else:
        if numero>ocorrencia:
            resposta= (-1) 
    return resposta