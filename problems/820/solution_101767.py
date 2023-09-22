def posLetra(frase, letra, ocorrencia):
    """Retorna a posicao da frase dado uma frase, uma letra e um numero inteiro str,str,int-> int"""

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