def retira_pontuacao(texto):
    if ':' in texto:
        texto= texto.replace(' ')
    if '-' in texto:
        texto= texto.replace(' ')
    if ';' in texto:
        texto= texto.replace(',')