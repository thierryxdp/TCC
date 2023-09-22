def posLetra(frase, letra, ocorrencia):
    '''Retorna a posição de uma frase em que a ocorrência
    de uma letra está, dados uma frase, uma letra e um número
    indicando a ocorrência da letra, caso exista menos ocorrências
    da letra do que a ocorrência pedida, a função retorna -1
    string, string, int -> int '''
    
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