def maiores (lista, n):
    """dada uma lista de numeros inteiros e um numero inteiro, retorna outra lista contendo o numero e os numeros maiores que ele da lista anterior;
    list,int->list."""
    d=[n]
    list.extend(lista,d)
    list.sort(lista)
    nova=list.index(lista,n,1)
    new=lista[nova:]
    return new