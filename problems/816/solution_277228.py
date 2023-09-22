def maiores(lista,n):
    ''' função que retorna os numeros inteiros de uma lista maiores que n,caso n for maior retorna uma lista vazia'''
 
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    b=a+1
    return lista[b:]