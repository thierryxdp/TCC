def retira_pontuacao(frase):
    "Função que "
    frase = frase.replace('-', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('...', ' ')
    
    return frase