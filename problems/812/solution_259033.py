def retira_pontuacao(frase):
    texto = frase.replace('!', ' ')
    texto = texto.replace('?', ' ')
    texto = texto.replace('...', ' ')
    texto = texto.replace('.', ' ')
    texto = texto.replace(',', ' ')
    texto = texto.replace('—', ' ')
    texto = texto.replace(':', ' ')
    texto = texto.replace(';', ' ')
    texto = texto.replace('-', ' ')
    return texto