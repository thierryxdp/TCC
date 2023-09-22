def maiores(lista,num):
    lista.append(num)
    lista.sort()
    index = index(num)+1
    lista.remove(num)
    return lista[index:]