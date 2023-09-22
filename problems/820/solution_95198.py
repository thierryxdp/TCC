def posLetra(string, letra, n):
    """funçao que retorna a posiçao da ocorrência n da letra na string
    str, str, int -> int"""
    if n <= str.count(string,letra):
        indice = 0
        verificacao = 1 
        while verificacao < n:
            indice = str.index(string,letra,indice + 1)
            verificacao += 1
        return indice
    else:
        return -1