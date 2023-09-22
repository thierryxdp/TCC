def retira_pontuacao(frase):
    '''Função que susubstitui a pontuação por espaço'''
    frase = str.split(frase,",")
    frase = str.join(" ", frase)
    return frase