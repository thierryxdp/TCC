def posLetra(frase,letra,ocorrencia):
    """str,str,int==>int"""
    acumulador=[]
    contador=0
    while contador < len(frase):
        if frase[contador]==letra:
            acumulador=acumulador+list(frase[contador])
        contador=contador+1
    return acumulador[ocorrencia-1]