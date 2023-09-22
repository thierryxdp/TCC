def inverte(frase):
    '''Essa função recebe uma frase e retorna ela invertida e sem pontuação'''
    return retira_pontuacao(str.reverse(frase))