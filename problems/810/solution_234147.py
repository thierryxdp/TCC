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
    palavras = str.split(retira_pontuacao(frase))
    list.reverse(palavras)
    return str.join(' ', palavras)