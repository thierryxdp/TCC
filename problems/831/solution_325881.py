def lingua_p(palavra):
    '''Traduz e retorna uma palavra dada para a língua do P 
    string -> string'''
    str.lower(palavra)
    lista = list(palavra)
    listap = []
    i = 0
    while i < len(lista):
        if lista[i] in 'aeiou':
            list.append(listap,lista[i])
            list.appen(listap,'p')
            list.append(listap,lista[i])
        else:
            list.append(listap,lista[i])
        i = i + 1
    return str.join('',listap)