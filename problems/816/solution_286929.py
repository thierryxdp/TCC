def maiores(N,n):
   '''função em que dada uma lista de números inteiros e um
   número inteiro n, retorna outra lista, contendo todos os
   números da lista de origem com numeros maior que n, em ordem crescente;
   list,int -> list'''
   if n in N:
    list.sort(N)
    lista=list.index(N,n)
    return N[lista+1]
   else:
        list.append(N,n)
        list.sort(N)
        lista=list.index(N,n)
        return N[lista+1:]