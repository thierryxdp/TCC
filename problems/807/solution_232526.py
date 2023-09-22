def retira_pontuacao(frase):
    """ Retira todas as pontuações do texto e as substitui por espaçoes"""
    pontuação = [';',':',',','.','-','!','...']
    for i in pontuação:
        frase = str.replace(i,' ')
    return frase