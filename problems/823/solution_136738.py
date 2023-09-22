def faltante(lista):
    '''Funçao que retorna um numero inteiro que está faltando no intervalo da lista dada na entrada
    list -> int'''
    i = 0 
    while i <= len(lista):
        if i + 1 not in (lista):
            return i + 1
        i = i + 1