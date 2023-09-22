def faltante(L):
    '''dada uma lista L de tamanho N-1 inteiros numerados de 1 a N, retorna
    o número inteiro deste intervalo que está faltando; list -> int'''
    a = 0
    L1 = L[:]
    b = list(range(len(L) + 2))
    c = sum(L)
    contagem = 0
    while contagem < len(L1):
        if len(L) == 1 and L[0] == 1:
            return 2
        elif len(L) == 1 and L[0] == 2:
            return 1
        else:
            return sum(b) - c
        
        contagem = contagem + 1