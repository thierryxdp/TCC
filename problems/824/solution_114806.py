def uppCons(frase):
    '''retorna a frase de entrada com todas as consoantes em maiusculas'''
    '''str -> str'''
    i = 0
    resposta = ''
    
    while i < len (frase):
        texto=frase[i]
        if texto not in 'aeiou':
            texto = str.upper(texto)
        resposta = resposta + texto
        i = i + 1
    return resposta