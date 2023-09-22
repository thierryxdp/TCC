def posLetra(frase,letra,n):
    '''função que dado como entrada uma string frase,uma letra e um numero
    n que indica a ocorrência desejada da letra(1 para primeira e assim
    por diante), retorna em que posição da frase a ocorrência está;
    str,str.int-->int'''
    
    proximo=0
    indices=[]
    
    if frase.count(letra)<n:
        return -1
    while proximo<len(frase):
        if letra in frase[proximo]:
            list.append(frase,proximo)
        proximo=proximo+1
    return indices[n-1]