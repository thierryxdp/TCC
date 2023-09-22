def maiores(lista,n):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    lista = lista + [n]
    nova = list.sort(lista)
    nova = list.index(nova,n)
    maior = nova[nova+1:]
    return maior