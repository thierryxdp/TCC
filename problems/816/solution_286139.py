def maiores(lista_num,n):
    """Funçao que dada uma lista de numeros inteiros e um numero inteiro(n),
    retorna outra lista, contendo todos os numeros da lista original
    maiores que n, em ordem crescente"""
    list.append(lista_num,n)
    list.sort(lista_num)
    lista_num2 = list.sort(lista_num)
    if max (lista_num) > n:
        return list.sort(lista_num2)