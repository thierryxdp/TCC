def filtraMultiplos(lista,n):
    "retorna uma lista contendo todos os elementos da lista original que forem divisíveis por n"
    listaa = ()
    i = 0
    while i < len(lista):
        if int(lista[i])%n == 0:
            listaa = listaa + (lista[i],)
        i = i + 1
    return list(listaa)