def faltante(numeros):
    i=0
    retorno=0
    if numeros[0]!=1:
            return 1
    while i<len(numeros):
        if numeros[i]!=numeros[i+1]+1:
            return numero[i]+1
        i+=1
    else:
        return len(numeros)+1