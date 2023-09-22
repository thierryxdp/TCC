def maiores(lista, n):
    """função que dada uma lista de numeros inteiros,retorna outra lista,list-->list"""
    lista = []
    n = 1
    lista_final = []
    for elemento in lista:
        if elemento > n:
            list.sort(lista)
             list.sort(elemento)
            lista_final.append(elemento)
            return[i for i in lista if i > n]