def melhor_volta(m):
    '''Função que dada uma matriz retorna o menor valor encontrado, a
    linha em que foi encontrado e o valor em si. list -> tuple'''
    if min(m[0]) < (min(m[1]) and min(m[2]) and min(m[3]) and min(m[4]) and min(m[5])):
        return (1, min(m[0]), (list.index(m[0], min(m[0])) + 1))
    if min(m[2]) < (min(m[0]) and min(m[1]) and min(m[3]) and min(m[4]) and min(m[5])):
        return (3, min(m[2]), (list.index(m[2], min(m[2])) + 1))
    if min(m[3]) < (min(m[0]) and min(m[1]) and min(m[2]) and min(m[4]) and min(m[5])):
        return (3, min(m[3]), list.index(m[3], min(m[3])))
    if min(m[4]) < (min(m[0]) and min(m[1]) and min(m[2]) and min(m[3]) and min(m[5])):
        return (4, min(m[4]), list.index(m[4], min(m[4])))
    if min(m[5]) < (min(m[0]) and min(m[1]) and min(m[2]) and min(m[3]) and min(m[4])):
        return (6, min(m[5]), (list.index(m[5], min(m[5])) + 1))
    else:
        return None