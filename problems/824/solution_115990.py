def uppCons(frase):
    ''' Função que transforma todas as consoantes em 
    maiusculo enquanto as vogais ficam em
    minusculo. Claro, ao ser dado uma FRASE com consoantes e vogais.
    str -> str'''
    
    contador = 0
    resultado = ''
    while contador < len(frase):
        if frase[i] not in 'aeiouãéíóú':
            resultado += frase[contador].upper()
        else:
            resultado += frase[contador].lower()
        contador += 1

    return resultado