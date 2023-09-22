def posLetra(string, letra, n):
    """funçao que retorna a posiçao da ocorrência n da letra na string
    str, str, int -> int"""
    if n <= str.count(string,letra):
        indice = 0
        verificacao = 2 
        indice = str.index(string,letra,indice)
        while verificacao <= n:
            indice = str.index(string,letra,indice+1)
            verificacao += 1
        return indice
    else:
        return -1