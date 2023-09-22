def uppCons(frase):
    '''Esta função retorna a frase de entrada com todas as consoantes
    em maiúsculo.
    str -> str'''
    contador = 0
    indice = 0
    while contador < len(frase):
        if frase[indice] in 'BCDFGHJKLMNPQRSTVXWYZÇbcdfghjklmnpqrstvxwyzç':
       	frase = frase[:indice] + str.upper(frase[indice]) + frase[indice+1:]
        else:
            frase = frase
        contador = contador + 1
    	indice = indice + 1
    return frase