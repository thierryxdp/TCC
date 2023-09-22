def faltante(L):
    """A função recebe uma lista com N - 1 inteiros numeros de 1 a N, e 
    retorna qual o número inteiro deste intervalo que está faltando. Isto é,
    igualmente ao número da peça que está faltando do quebra-cabeço de João;
    list -> int"""
    
    L.sort()
    i = 0
    
    if L[0] != 1:
        return 1
  
    while i<=len(L):
        if L[0] == 1 and (L[i] - L[i-1]) == 1:
            return L[-1]+1
        i = i + 1
        if (L[i] - L[i-1]) != 1:
            return int((L[i] + L[i-1])/2)
        i = i + 1