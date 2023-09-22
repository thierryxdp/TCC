def maiores(lista,n):
    "Retorna todos os numeros da lista maiores que n. list,int->list"
    list.reverse(lista)
    list.append(lista,n)
    list.reverse(lista)
    posi = list.index(lista,n)
    return lista[:posi]