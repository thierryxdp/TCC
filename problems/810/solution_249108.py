def retira_pontuacao(frase):
    '''Faça uma função que retorne uma frase sem pontuacao, str -> str'''
    pontuacao = str(' ')
    frase = str.replace(frase,',',pontuacao).replace('.',pontuacao).replace('-',pontuacao).replace('?',pontuacao).replace('!',pontuacao)
    return frase

def inverte(frase):
    '''Faça uma funcao que retorne uma frase em minúsculo, str -> str'''
    return str.lower(frase)