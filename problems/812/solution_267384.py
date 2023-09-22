def retira_pontuacao(frase):
    resultado=frase.replace(',', ' ')
    resultado=frase.replace('?', ' ')
    resultado=frase.replace('.', ' ')
    resultado=frase.replace(';', ' ')
    resultado=frase.replace('-', ' ')
    resultado=frase.replace('!', ' ')
    resultado=frase.replace(':', ' ')
    return resultado