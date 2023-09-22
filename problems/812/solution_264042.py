def retira_pontuacao(frase):
    '''Faça uma função que dada a frase retorne a frase com todos os caracteres substituídos por espaço, str -> str'''
    pontuacao = ''
    remover = ',','.','?','!'
    return str.replace(frase, pontuacao, del(remover))