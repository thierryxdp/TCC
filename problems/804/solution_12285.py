def filtra_pares(a):
    '''
    Dado uma tupla com quatro elementos inteiros 
    retorna uma nova tupla apenas com os numeros pares;
    tuple -> tuple

    '''
    tuplas = ()
    if a[0] % 2 == 0:
        tupla = tupla + (a[0],)
    if a[1] % 2 == 0:
        tupla = tupla + (a[1],)
    if a[2] % 2 == 0:
         tupla = tupla + (a[2],)
    if a[3] % 2 == 0:
         tupla = tupla + (a[3],)
    return tupla