def retira_pontuacao(frase):
    texto = frase.replace('!', ' ').replace('?', ' ').replace('...', ' ').replace('.', ' ')
    texto = texto.replace(',', ' ').replace('—', ' ').replace(':', ' ').replace(';', ' ')
    texto = texto.split()
    return ' '.join(texto)