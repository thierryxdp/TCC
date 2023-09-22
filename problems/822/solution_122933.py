def repetidos(L):
    """Função que receba como entrada uma lista de números, e retorne o número de vezes que um elemento da lista é igual
    ao elemento anterior."""
    i = 1
    r = 0
    while (len(L)>i):
        if L[i] == L[i-1]:
           r = r + 1 
        i = i  + 1
    return r