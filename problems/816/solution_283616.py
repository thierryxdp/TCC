def insere(lista,n):
    list.append(lista,n)
    list.sort(lista)
    return lista

def maiores(lista,n):
    num=insere(lista,n)
    list.reverse(num)
    indice=list.index(num,n)
    list.reverse(num)
    return num[(indice)*-1:]