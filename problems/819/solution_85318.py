def filtraMultiplos(lista, n):
    '''Funcao que recebe uma lista e um numero e retorna uma lista com todos os elementos que forem divisiveis por n
    List, Int -> List'''
    mult =[]
    for a in lista:
        if a%n ==0:
            mult.append(a)
    return mult