def posLetra (string, letra, i):
    '''Encontra a posição de uma letra dado sua ocorrência (1ª, 2ª, 3ª, etc) em uma string
    string, string, int -> int'''
    if str.count (string, letra) < i:
        return -1
    elif i == 1:
        return str.find (string, letra)