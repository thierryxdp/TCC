def maiores(lista,n):
    '''Dada uma lista de números inteiros e um numero 
    inteiro n, a função retorna uma outra lista contendo 
    apenas os numeros maiores que n da lista de entrada em 
    ordem crescente. list,int -> list'''
    x=lista
    if n not in x:
        list.append(x,n)
    list.sort(x)
    y=list.index(x,n)
   
   
   
    return x[y+1:]