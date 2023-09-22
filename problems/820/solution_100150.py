def posLetra(string,letra,num):
    i = 0
    lista = []
    while i<len(string):
        if string[i] == letra:
            lista.append(i)
        i = i + 1
        
    
    if len(lista) >= num:
        return lista[num-1]
    elif len(lista)<num:
        return -1