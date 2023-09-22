def insere(lista,n):
    list.append(lista,n)
    list.sort(lista)
    return lista

def maiores(lista,n):
    num=insere(lista,n)
    indice=list.index(num,n)
    if n in lista:
        list.reverse(num)
        indice1=list.index(num,n)
        list.reverse(num)
        return num[(indice1)*-1:]
    elif indice+1>=len(num):
        return []
    else:
        return num[indice +1:]