def maiores(N,n):
   '''função em que dada uma lista de números inteiros e um
   número inteiro n, retorna outra lista, que contenha todos os
   números da lista original maiores que n, ordenados em ordem crescente;
   list,int -> list'''
   if n in range N:
    list.sort(N)
    lista=list.index(N,n)
     return N[lista+1:]
    else:
        list.append(N,n)
        list.sort(N)
        lista=list.index(N,n)
        retun N[lista+1:]