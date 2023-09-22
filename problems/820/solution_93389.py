def posLetra(string,letra,n):
    """É dado como entrada uma string, uma letra, e um número natural
n. A função retorna a posição da letra após a n-ésima ocorrência, dada 
por um número natural. Caso exista menos ocorrências da letra do que a ocorrência pedida,
a função retornará -1; string,string,int->int"""
    i=0
    acumulador=[]
    while i<len(string):
        if string[i]==letra:
            acumulador+=[i]
        i+=1
    if len(acumulador)<n:
        return -1
    else:
        return acumulador[n-1]