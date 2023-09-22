def faltante(L):
    """Funçao que recebe uma lista com numeros interiros numerados e descubra qual é o numero
que esta faltando naquele intervalo de numeros list->int""" 
    i 0
    while i < len(L):
        if L[0] != 1:
            return 1
        elif len(L) == L[-1]:
            return L[-1]+1
        elif (L[i] != L[i+1]-1):
            return L[i]+1
        i = i+1