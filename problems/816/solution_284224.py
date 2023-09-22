def maiores(lista,n):
    """Funçao que dada ums lista de numeros inteiros e um numero inteiro n, retorna outra lista contendo todos os numeros
    da lista orgirinal maiores que n em ordem crescente;
    list,int-->list"""
    list.append(lista,n)
    list.sort(lista)
    lista_final = list.index(lista,n)
    return lista[lista_final+1:]