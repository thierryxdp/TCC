def maiores(lista,n):
    """
    Retorna a lista dada com os numeros maiores que n ordenados em ordem crescente;
    list, int -> list
    """
    lista = lista + [n]
    nova = list.sort(lista)
    index = list.index(nova,n)
    maior = nova[index+1:]
    return maior