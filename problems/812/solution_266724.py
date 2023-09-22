def retira_pontuacao(frase):
    """ Retira todas as pontuações do texto e as substitui por espaçoes"""
    pontuacao = [';',':',',','.','-','!','...']
    for i in pontuacao:
        frase = str.replace(frase,i, ' ')
    return frase