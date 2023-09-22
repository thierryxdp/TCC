def inverso(string):
    '''inverte as palavras sem pontuação e com todas as letras minúsculas
    str -> str'''
    frase=frase.lower
    frase=frase.replace('.' , ' ')
    frase=frase.replace(',' , ' ')
    
    return str.join(-1,str.split(frase))