def conta_frases (frase):
    '''Função que,dado um texto, retorna a quantidade de frases contidas no mesmo através do número de caracteres de pontuação;
    str->int'''
    
    f1=str.replace(frase,'.','x')
    f2=str.replace(f1,'!','x')
    f3=str.replace(f2,'...','x')
    f4=str.replace(f3,'?','x')
    f5=str.replace(f4,'xxx','x')
    
    return len((str.split(frase,'x')))