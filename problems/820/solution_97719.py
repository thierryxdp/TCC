def posLetra(string: str, letra: str, n: int)-> int:
    """Dados uma string, uma letra e um número "n" que indica a ocorrência
    desejada da letra. A função retorna em que posição da string aquela
    ocorrência da letra está. Caso exista menos ocorrências da letra
    do que a ocorrência pedida, a função retorna: -1"""
    string = list(string)
    i = 0
    ocorrencia = 0
    if list.count(string, letra) < n:
        return -1
    else:
        while (i < len(string)):
            if (letra == string[i]):
                ocorrencia += 1
                if (ocorrencia == n):
                    return i
            i += 1