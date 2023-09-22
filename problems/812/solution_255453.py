def retira_pontuacao(frase):
    '''uma função que substitui todos os caracteres de pontuação de uma frase por espaço
    str -> str'''
    nfrase  = str.replace(frase,"?"," ")
    return nfrase