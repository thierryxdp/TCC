def maiores(lista_inteiros,n):
    """Funcao que dada uma lista de numeros inteiros e um numero n, retorna
    outra lista composta por todos os numeros da lista original maiores que n;
    list,int->list"""

    if list.count(lista_inteiros,n) >= 1:
        
        list.sort(lista_inteiros)
        indice = list.index(lista_inteiros,n)
        del lista_inteiros[0:indice+1]
    
        return lista_inteiros

    else:

        list.append(lista_inteiros, n)
        list.sort(lista_inteiros)
        indice = list.index(lista_inteiros,n)
        del lista_inteiros[0:indice+1]
    
        return lista_inteiros