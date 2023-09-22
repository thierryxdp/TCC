def inverte(frase):
    '''Faça uma função que retorne a frase de ordem inversa, letras minúsculas e sem pontuação, str -> str'''
    pontuacao = str(' ')
    return (str.lower(str.replace(frase,',',pontuacao).replace('.',pontuacao).replace('-',pontuacao).replace('?',pontuacao).replace('!',pontuacao)))