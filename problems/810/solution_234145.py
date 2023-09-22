def retira_pontuacao (frase):
    frase = str.replace(frase, '...', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, ':', ' ')
    return frase

def inverte(frase):
    return str.join(' ', str.split(frase))