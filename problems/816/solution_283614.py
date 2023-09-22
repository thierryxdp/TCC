def maiores(lista,n):
    num=insere(lista,n)
    list.reverse(num)
    indice=list.index(num,n)
    list.reverse(num)
    return num[(indice)*-1:]