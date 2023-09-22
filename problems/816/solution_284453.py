def maiores(lista_num,n):
    lista_num.append(n)
    lista_num.sort()
    return lista_num[lista_num.index(n):len(lista_num)+1]