def retira_pontuacao(frase):
    for a in '.!?,.;:-':
        frase = frase.replace(a,' ')
    return frase