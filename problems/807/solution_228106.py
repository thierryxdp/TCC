def conta_frases (frase):
    '''Função que,dado um texto, retorna a quantidade de frases contidas no mesmo através do número de caracteres de pontuação;
    str->int'''
    
    f1=frase.replace('.', 'x')
    f2=f1.replace('!', 'x')
    f3=f2.replace('...', 'x')
    f4=f3.replace('?', 'x')
    f5=f4.replace('xxx', 'x')
    
    return len((str.split(f5,'x')))