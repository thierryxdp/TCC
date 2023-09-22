def retira_pontuacao(texto):
    for x in '.:;-,?!':
        texto=texto.replace(x,'')
    return texto