def maiores(lista,num):
    lista.append(num)
    lista.sort()
    index = lista.index(num)
    lista.remove(num)
    return lista[index:]