def faltante(inteiros):
    '''recebe uma lista com numeros inteiros e retorna o numero que está faltando'''
    inicio = 0
    list.sort(inteiros)
    N = len(inteiros)
    proximo = 1
    ordem = []

    while inicio <= N:
        if N == 1:
            if ((inteiros[0])-1) == 1:
                return 1
            else:
                return inteiros[0]+1
            
        if inteiros[proximo] > (N - 1):
            falta = (inteiros[-1] + 1)
            break
            
        if inteiros[0] != 1:
            falta = 1
            break
            
        if inteiros[inicio] == ((inteiros[proximo])-1):
            ordem = ordem + [inteiros[inicio]]
            inicio = inicio + 1
            proximo = proximo + 1
            
        if inteiros[inicio] != ((inteiros[proximo])-1):
            ordem = ordem + [inteiros[inicio]]
            falta = ((ordem[-1]) + 1)
            break

    return falta