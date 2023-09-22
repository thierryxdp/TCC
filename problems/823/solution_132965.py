def faltante(lis):
    """ Função que retorna o numero faltante dentro da lista fornecida;
        list -> int"""
    list.sort(lis)
    ultimoindice = lis[-1]+2
    liscomp = list(range(1,ultimoindice))
    i = 0
    
    while i <len(liscomp):
        if liscomp[i] in lis:
            i += 1
        elif liscomp[i] not in lis:
            return liscomp[i]