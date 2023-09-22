def retira_pontuacao(frase):
    '''Faça uma função que dada a frase retorne a frase com todos os caracteres substituídos por espaço, str -> str'''
    frase = ''
    pontuacao = ',', '.', '?', '!'
    remover = ' '
    return str.replace(frase,pontuacao, remover)