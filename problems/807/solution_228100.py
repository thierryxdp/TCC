def conta_frases (frase):
    '''Função que,dado um texto, retorna a quantidade de frases contidas no mesmo através do número de caracteres de pontuação;
    str->int'''
    
    frase=str.replace('.','x')
    frase=str.replace('!','x')
    frase=str.replace('...','x')
    frase=str.replace('?','x')
    
    return len(str.split(x))