def lingua_p(palavra):
    '''Retorna a palavra fornecida inserindo, após cada vogal, 'pe'.
    str -> str'''
    lista = list(str.lower(palavra))
    tamanho = range(len(lista))
    for i in tamanho:
        if lista[i] in 'aeiouãáéíõóú':
            lista[i] = lista[i]+'p'+lista[i]
    return str.join('',lista)