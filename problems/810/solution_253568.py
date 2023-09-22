def inverte(frase):
    '''função que recebe uma frase, inverte e remove a pontuação'''
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = ' '.join(frase)
    return(frase)