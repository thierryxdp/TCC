def lingua_p(palavra):
    '''Traduz e retorna uma palavra dada para a língua do P 
    string -> string'''
    str.lower(palavra)
    lista = list(palavra)
    listap = []
    i = 0
    while i < len(lista):
        if lista[i] in 'aeiouáéíóúâêôãõ':
            list.append(listap,lista[i])
            list.append(listap,'p')
            list.append(listap,lista[i])
        else:
            list.append(listap,lista[i])
        i = i + 1
    return str.join('',listap)