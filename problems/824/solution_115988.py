def uppCons(frase):
    ''' Função que transforma todas as consoantes em 
    maiusculo enquanto as vogais ficam em
    minusculo. Claro, ao ser dado uma FRASE com consoantes e vogais.
    str -> str'''
    
    i = 0
    resultado = ''
    while i < len(frase):
        if frase[i] not in 'aeiouãéíóú':
            resultado += frase[i].upper()
        else:
            resultado += frase[i].lower()
        contador += 1

    return resultado