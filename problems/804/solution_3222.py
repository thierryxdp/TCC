def filtra_pares (tupla):
    """Funçao que recebe uma tupla com quatro numeros inteiros e retorna uma nova tupla filtrando os numeros pares;
    entrada: tuple (int, int, int, int);
    saida: tuple."""
      pares = ()
    if tupla [0] % 2 == 0:
        par = (tupla [0], )
    if tupla [1] % 2 == 0:
        par = par + (tupla [1], )
    if tupla [2] % 2 == 0:
        par = par + (tupla [2], )
    if tupla [3] % 2 == 0:
        par = par + (tupla [3], )
    return par