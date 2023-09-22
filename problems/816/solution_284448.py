def indice(lista_num,n):
    lista_num.append(n)
    lista_num.sort()
    return lista_num.index(n)

def maiores(lista_num,n):
    return lista_num[n,len(lista_num)+1]