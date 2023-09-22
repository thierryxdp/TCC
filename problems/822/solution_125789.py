rom collections import defaultdict
def repetidos (lista):
    '''retorne o numero de vezes que um elemento da lista e igual ao anterior'''
    lista = [3, 2, 4, 7, 3, 8, 2, 3, 8, 1]
    keys = defaultdict(list);
    for key, value in enumerate(lista):
        keys[value].append(key)
    for value in keys:
        if len(keys[value]) > 1:
            return(value, keys[value]