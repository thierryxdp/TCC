def conta_numero(num,ls):
    """Essa função serve para contar o número de vezes que um número
    inteiro (num) aparece na matriz (ls)
    int,list->int"""
    vzs = 0
    for listas in ls:
        for numero in listas:
            if numero == num:
                vzs += 1
    return vzs

#conta_numero(7,[[1,2,3],[4,5,6],[7,8,9]]) == 1
#conta_numero(1,[[1,1],[1,1]]) == 4
#conta_numero(111,[[555,666],[777,888]]) == 0