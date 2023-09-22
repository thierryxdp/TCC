def posLetra(frase, letra, ocorrencia):
    """dado uma frase, uma letra e um numero que indica a ocorrência
    desejada da letra, retornara em que posiçao da frase a ocorrencia
    esta. caso exista menos ocorrencias da letra do que a pedida, a funcao
    deve retornar -1.
    str, str,str --> int"""
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