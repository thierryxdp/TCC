def lingua_p(palavra):
    '''Traduz e retorna uma palavra dada para a língua do P 
    string -> string'''
    str.lower(palavra)
    listap = list(palavra)
    i = 0
    while i < range(listap):
        if listap[i] == 'aeiouáéíóúãõàâêô':
            list.insert(listap,i,listap[i])
            list.insert(listap,i+1,'p')
        i = i + 1
    return str.join(listap)