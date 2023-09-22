def retira_pontuacao(frase):
    for a in '.!?,.;:-':
        frase = frase.replace(a,' ')
    return frase


def inverte(frase):
    frase = ''.join(frase)
    frase1= retira_pontuacao(frase)
    frase2= frase1.split()
    frase3= frase2[::-1]
    return ' '.join(frase3)