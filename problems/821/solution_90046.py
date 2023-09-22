def fatorial(n):
    '''Função que retorna o fatorial de um número
    int -> int'''
    i = 1
    fatorial = 1
    auxiliar = n
    while i<n:
       auxiliar = auxiliar*i 
       i = i + 1
    return auxiliar