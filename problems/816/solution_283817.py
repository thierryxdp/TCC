def maiores(lista,n):
    '''Essa funcao que dada uma lista de numeros inteiro e um numero  inteiro n, retorna outra lista com todos os numeros maiores que n de forma crescente'''
    '''int,int=>int'''
    maiores=list()
    lista.sort()
    for c in lista:
       if c >= n:
        maiores.append(c)
    return maiores