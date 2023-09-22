def posLetra(frase, letra, ocorrencia):
    '''
    Dado uma frase, uma letra e um número inteiro indicando a ocorrência,
    retorna a posição da frase em que aquela ocorrência da letra se encontra.
    str, str, int->int
    '''
    if frase.count(letra) < ocorrencia:
        return -1
    else:
        x = 0
        letras = []
        caracteres = list(frase)
        while x < len(caracteres) and len(letras) < ocorrencia:
            if letra == caracteres[x]:
                list.append(letras, caracteres[x])
            x = x + 1
        return x - 1