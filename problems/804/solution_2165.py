def filtra_pares(numeros):
    """uma função que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas elementos pares;
       tupla -> tupla"""
    pares= ()
    if numeros[0] % 2 == 0:
        pares += (numeros[0],)
    if numeros[1] % 2 == 0:
        pares += (numeros[1],)
    if numeros[2] % 2 == 0:
        pares += (numeros[2],)
    if numeros[3] % 2 == 0:
        pares += (numeros[3],) 
    return pares