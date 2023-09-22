def maiores (lista, n):
    """funçao que recebe uma lista de numeros inteiros e um numero n e retorna a lista apenas com todos os numeros maiores do que o numero n;
    entrada: list, int
    saida: list."""
    
    list.sort (lista)
    del (lista [:n:])
    
    return lista