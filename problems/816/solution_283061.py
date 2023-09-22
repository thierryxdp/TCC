def maiores(l,n):
    '''Dada uma lista com números inteiros e um n também 
    inteiro, retorna outra lista apenas com os inteiros 
    maiores que n ordenada
    list,int -> list'''
    if n not in l:
        list.append(l,n)
    list.sort(l)
    posN = list.index(l,n)
    nova = l[(posN + 1):]
    return nova