def maiores(x,n):
    lista = []
    tamanho = len(x)
    if x[0:tamanho+1:100] > [n]:
        list.append(lista,x[0])
    else:
        lista = lista
    if x[1:tamanho+1:100] > [n]:
        list.append(lista,x[1])
    else:
        lista = lista
    if x[2:tamanho+1:100] > [n]:
        list.append(lista,x[2])
    else:
        lista = lista
    if x[3:tamanho+1:100] > [n]:
        list.append(lista,x[3])
    else:
        lista = lista
    if x[4:tamanho+1:100] > [n]:
        list.append(lista,x[4])
    else:
        lista = lista
    if x[5:tamanho+1:100] > [n]:
        list.append(lista,x[5])
    else:
        lista = lista
    if x[6:tamanho+1:100] > [n]:
        list.append(lista,x[6])
    else:
        lista = lista
    lista.sort()
    return lista