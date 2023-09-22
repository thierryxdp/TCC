def retira_pontuacao(frase):
    '''Faça uma função dada uma frase retorne a frase com os caracteres de pontuação substituído por espaço, str -> str'''
    pontuacao = str(' ')
    return frase.replace(',',pontuacao).replace('.',pontuacao).replace('-',pontuacao).replace('?',pontuacao).replace('!',pontuacao)