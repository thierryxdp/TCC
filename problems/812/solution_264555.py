def retira_pontuacao(frase):
    s = str.replace(frase, ',', '') 
    s = str.replace(frase, '.', '')
    s = str.replace(frase, '!', '')
    s = str.replace(frase, '?', '')
    s = str.replace(frase, '-', '')
    s = str.replace(frase, ':', '')
    s = str.replace(frase, ';', '')
    return s