def posLetra(frase, letra, n):
    """Função que nos retorna a posição da string em que determina ocorrência da letra está. Caso exista menos ocorrências da letra do que a ocorrência pedida a função retorna -1.
    (str, str, int) -> int """

    i = 0
    ocorrencia = 0

    while i <= (len(frase)-1) and ocorrencia <= n - 1:
        if frase[i] == letra:
            ocorrencia = ocorrencia + 1
            

        i = i + 1


    if ocorrencia < n:
        return -1

    else:
        return i - 1