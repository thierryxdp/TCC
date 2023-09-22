def faltante(inteiros):
    '''recebe uma lista com numeros inteiros e retorna o numero que está faltando'''
    inicio = 0
    list.sort(inteiros)
    N = len(inteiros)
    proximo = 1
    ordem = []

    while inicio < N:
        
        if inteiros[inicio] == ((inteiros[proximo])-1):
            inicio = inicio + 1
            proximo = proximo + 1
            ordem = ordem + [inteiros[inicio]]
        if inteiros[inicio] != ((inteiros[proximo])-1):
            return ((ordem[-1])+1)