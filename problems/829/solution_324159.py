def soma_h(h):
    lista = [1]
    for c in range(1,h+1):
        i = (1/c)
        lista.append(i)
    return sum(lista,2)