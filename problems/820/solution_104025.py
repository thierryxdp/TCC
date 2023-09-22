def posLetra(f, l, o):
    """
    Essa função recebe uma frase 'f', uma letra 'l' e um número inteiro 'o'
    indicando a ocorrência, retorna em que posição da string aquela ocorrência
    da letra está.
    Parametros de entrada: str, str, int
    Valor de saida: int
    """

    if f.count(l)<o:
        return -1
    else:
        i = 0
        posicao = []
        caracteres = list(f)
        while i < len(caracteres) and len(posicao)<o:
            if l == caracteres[i]:
                list.append(posicao, caracteres[i])
            i = i + 1
        return i-1