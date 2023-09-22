def retira_pontuacao(texto):
    for X in '-,:;.':
        texto=texto.replace(X,'')
    return texto