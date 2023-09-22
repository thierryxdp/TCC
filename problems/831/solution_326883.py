def lingua_p(palavra):
    lista = []
    i = 1
    nova_palavra=''
    while (i < len(palavra)):
        lista = [palavra[i],]
        i += 1
        if (lista[i] in 'aeiou'):
            lista = lista.insert(i,'p'+lista[i])
    return lista