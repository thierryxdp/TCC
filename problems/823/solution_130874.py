def faltante(L):
    '''A função recebe uma lista L com N-1 inteiros numerados de 1 a N e retorna o número
    inteiro x deste intervalo que está faltando.
    Parâmetro de entrada: list
    Valor de retorno: int'''
    list.sort(L)
    i=0
    x=0
    #Caso o número faltando seja igual a 1
    if L[0]!=1:
        x=1
    #Caso o número faltando seja diferente de 1
    while i<len(L)-1:
        if L[i]+1!=L[i+1]:
            x=L[i+1]-1
        i=i+1
    #Caso o número faltando seja N
    if x==0:
        x=len(L)+1   
    return x