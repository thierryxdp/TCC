def retira_pontuacao(frase):
    '''substitui os caracteres de pontuação de uma frase por espaços'''
    for char in "-,.?!:;":
        frase = frase.replace(char, " ")
    return frase