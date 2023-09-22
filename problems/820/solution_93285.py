def posLetra(frase, letra, n):
    """Recebe uma frase, uma letra e um número que indica
    a ocorrência (repetição) daquela letra.
    Retorna a posição da string em que está a ocorrência.
    Caso haja menos ocorrências do que o número dado,
    a função retorna -1.
    str, str, int->int"""
    i = 0
    ocorrencias = 0
    if n > frase.count(letra):
        return -1
    else:
        while i < len(frase) and ocorrencias < n:
            if frase[i]==letra:
                ocorrencias=ocorrencias+1
            i = i + 1
    return i-1