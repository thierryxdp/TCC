def retira_pontuacao(frase):
    '''Faça uma função dada uma frase retorne a frase com os caracteres de pontuação substituído por espaço, str -> str'''
    pontuacao = (' ')
    return frase.replace(',',pontuacao).replace('.',pontuacao)