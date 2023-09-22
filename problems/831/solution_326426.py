def lingua_p(palavra):
    lista = list(palavra)
    for i in range(len(lista)):
        if lista[i] in 'AEIOUaeiou':
            lista[i] = lista[i] + 'p' + lista[i]
    return ''.join(lista)