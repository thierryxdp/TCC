def posLetra (string, letra, n):
    """funcao que retorna em que posicao da str uma certa ocorrencia de letra esta
    str,str,int -> int"""
    resultado = string.count(letra)
    n = int(n)
    if (0 < n <= resultado):
        ocorrencia = -1
        while (n > 0):
            ocorrencia = string.index(letra, ocorrencia + 1)
            n = n -1
        return ocorrencia
    else 
    -1