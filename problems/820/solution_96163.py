def posLetra(frase,letra,ocorrencia):
    """str,str,int==>int"""
    acumulador=[]
    contador=0
    if str.count(frase,letra)<ocorrencia:
        return -1
    if str.count(frase,letra)>=ocorrencia:
        while contador < len(frase):
            if frase[contador]==letra:
                list.append(acumulador,contador)
            contador=contador+1
      
        return acumulador[ocorrencia-1]