def inverte(frase):
    frase= str.lower(frase)
    frase=retira_pontuacao(frase)
    frase1= str.split(frase,' ')
    resp= str.join(' ', frase1)
    return resp