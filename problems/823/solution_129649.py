def faltante(l):
    '''
    Esta função recebe uma lista de números inteiros com um números faltando e retorna o número inteiro 
    que está faltando.
    
    Parametros
    ----------
    l (list) : lista de números inteiros
    '''
    l = sorted(l)
    l0 = list(range(l[0], l[-1] + 1))
    c = 0
    if l[0] != 1:
        return 1
    if l0 == l:
        return l0[-1]+1
    while c <= len(l):
        if l[c] != l0[c]:
            return l0[c]
        c += 1
    return l0