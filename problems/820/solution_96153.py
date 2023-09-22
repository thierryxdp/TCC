def posLetra(frase,letra,ocorrencia):
    """str,str,int==>int"""
    acumulador=[]
    contador=0
    while contador < len(frase):
        if frase[contador]==n:
            acumulador=acumulador+frase[contador]
    return acumulador[ocorrencia-1]