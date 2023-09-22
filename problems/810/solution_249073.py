def inverte(frase):
    '''Faça uma função que retorne uma frase sem pontuacao, minúscula e invertida, str, list -> str'''
    pontuacao = str(' ')
    return str.lower(str.replace(frase,',',pontuacao).replace('.',pontuacao).replace('-',pontuacao).replace('?',pontuacao).replace('!',pontuacao))