def posLetra(stri,letra,num):
    i = 0
    lista = []
    while i<len(stri):
        if stri[i] = letra:
            lista.append(i)
        i = i + 1
        
    if len(lista) >= num:
        return lista[num + 1]
    else:
        return -1