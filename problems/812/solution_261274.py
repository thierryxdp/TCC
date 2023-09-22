def retira_pontuacao(frase):
    frase1 = str.replace(frase,',','.')
    frase2 = str.replace(frase1,'-','.')
    frase3 = str.split(frase2,'.')
    frase4 = str.join(' ', frase3)
    return frase4