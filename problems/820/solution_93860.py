def posLetra(string, letra, n):
    """dada uma string, uma letra, e um nnmero que indica a
    ocorrencia desejada da letra, função retorna a posiçao da
    string onde aquela ocorrencia da letra esta. str, str, int -> int"""
    pos = string.find(letra)
    while pos >= 0 and n > 1:
        pos = string.find(letra, pos + 1)
        n = n - 1
    return pos