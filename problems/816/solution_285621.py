def maiores(lista,n):
    ''''
    Funçção que dada uma lista de numeros inteiros(lista) e um numero inteiro(n), retorna outra lista,
    que contenha todos so numero da lista original maiores que n, em ordem crscente
    list -> list
    ''''
    list.append(lista,n)
    list.sort(lista)
    nyx=list.index(lista,n)
    return lista[nyx+1:]