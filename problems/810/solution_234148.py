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
    palavras = str.split(str.lower(retira_pontuacao(frase)))
    list.reverse(palavras)
    return str.join(' ', palavras)