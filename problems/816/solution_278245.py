def maiores (lista, n):
    """funçao que recebe uma lista de numeros inteiros, um numero n e retorna uma lista somente com os numeros maiores que n;
    entrada: list, int
    saida: list."""
    
    if n in lista:
        list.sort (lista)
        ocorrencia = list.index (lista,n)
        return lista [ocorrencia+1:]
    else:
        list.append (lista, n)
        list.sort (lista)
        ocorrencia = list.index (lista,n)
        return lista [ocorrencia+1:]