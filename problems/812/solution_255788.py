def retira_pontuacao(frase):
    s = frase.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace(':', ' ').replace('!', ' ').replace('?', ' ').replace('-', ' ').replace('...', ' ')
    return s