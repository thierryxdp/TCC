def posLetra(frase, letra, ocorrencia):
    '''
    Dado uma frase, uma letra e um número inteiro indicando a ocorrência,
    retorna a posição da frase em que aquela ocorrência da letra se encontra.
    str, str, int->int

    Uso:
    posLetra(frase, letra, ocorrencia)

    Entrada:
    - frase (str): Frase original
    - letra (str): Letra específica
    - ocorrência (str, int): Indica a ocorrência da letra na função deve procurar

    Saída:
    - Retorna a posição em que a string da ocorrencia se encontra. (int)
    '''

    if frase.count(letra) < ocorrencia:
        return -1
    else:
         i = 0
        letras = []
        caracteres = list(frase)
        while i < len(caracteres) and len(letras) < ocorrencia:
            if letra == caracteres[i]:
                  list.append(letras, caracteres[i])
            i = i + 1
         return i - 1