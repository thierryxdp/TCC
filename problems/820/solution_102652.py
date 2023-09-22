def posLetra(frase, letra, ocorrencia):
    '''Funçao que, fornecida uma frase, uma letra e um numero
    inteiro indicador da ocorrencia desejada da letra, retorna
    a posiçao da frase em que aquela ocorrencia da letra se 
    encontra
    str, str, int->int
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