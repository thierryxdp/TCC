def filtra_pares(x):
    """Cálculo de uma função que recebe uma tupla com quatro elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem que se encontravam."""
    tupla = ()
    if x[0] %2==0:
        tupla=tupla +(x[0],)
    if x[1] %2==0:
        tupla=tupla +(x[1],)
    if x[2] %2==0:
        tupla=tupla +(x[2],)
    if x[3] %2==0:
        tupla=tupla +(x[3],)
    return tupla