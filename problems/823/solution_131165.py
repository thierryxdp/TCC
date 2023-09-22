def faltante(L):
    """A função recebe uma lista com N - 1 inteiros como entrada, e 
    analisa qual inteiro está faltando dentro do intervalo de 1 a N peças. 
    Por exemplo: Entrada: [1,2,3,5]
    Saida: 4;
    list -> int"""
    L.sort()
    i = 1
    peca_faltante = 0
    while i<=len(L):
        if i != L[i-1]:
            peca_faltante = i
        i = i + 1
    return peca_faltante