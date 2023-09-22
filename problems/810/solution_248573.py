def inverte(frase):
    '''Faça uma função dada uma frase que a mesma possua ordem inversa, letras minúsculas e sem pontuação, str -> str'''
    pontuacao = str(' ')
    str.replace(frase,',',pontuacao).replace('.',pontuacao).replace('-',pontuacao).replace('?',pontuacao).replace('!',pontuacao)
    str.lower(pontuacao)
    return pontuacao