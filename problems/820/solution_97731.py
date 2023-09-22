def posLetra(string, letra, n):
    """Retrona em que posição da string a ocorrencia, n, da letra está;
       Entrada: str, str, int;
       Saida: int;
    """
    contador = 0
    posicao = []
    if string.count(letra) < n:
        return -1
    while contador < len(string):
        if string[contador] == letra:
            posicao.append(contador)
        contador = contador + 1
    return posicao[n - 1