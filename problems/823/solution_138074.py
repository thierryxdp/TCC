def faltante(L,n):
    '''função que retorna a peca faltante de um quebra cabeça dados uma lista n-1
lis->int'''
    proximo=0
    pecafaltante=[]
    while proximo<len(L):
        if n in not L:
            pecafaltante= max(L)+1
    proximo= proximo+1
    return pecafaltante