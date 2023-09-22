def posLetra(frase, letra, ocorrencia):
    '''função que retorna posição da ocorrência de uma letra numa frase
    dado os parâmetros frase, letra e número inteiro'''
    
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