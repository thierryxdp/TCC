def posLetra(string, letra, ocorrencia):
    '''dada uma string, uma letra e um numero indicando a ocorrencia
    desejada da letra, retorna em que posição da string, aquela 
    ocorrencia da letra está, e retorna -1 caso exita menos ocorrencias
    do que pedido
    str, str, int->int'''

    if string.count(letra) < ocorrencia:
        return -1
    
    else:
        i = 0
        letras = []
        caracteres = list(string)
        while i < len(caracteres) and len(letras) < ocorrencia:
            if letra == caracteres[i]:
                list.append(letras, caracteres[i])
            i = i + 1
        return i - 1