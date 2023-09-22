def posLetra (string, letra, i):
    '''Encontra a posição de uma letra dado sua ocorrência (1ª, 2ª, 3ª, etc) em uma string
    string, string, int -> int'''
    lista = str.split (string)
    if list.count (lista, letra) < i:
        return -1
    else:
        return o