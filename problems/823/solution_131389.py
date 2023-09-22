def faltante(L):
    """A função recebe uma lista de inteiros N - 1 e avalia dentro do 
    intervalo, qual a peça está faltando, e retorna o numero desta;
    list -> int"""
    
    L.sort()
    i = 1
    
    if L[0] != 1:
        return 1
  
    while i<len(L):
        if (L[i] - L[i-1]) != 1:
            return int((L[i] + L[i-1])/2)
        i = i + 1

    if L[0] == 1:
        return L[-1]+1