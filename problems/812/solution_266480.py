def retira_pontuacao(frase):
    """ Retira todas as pontuações do texto e as substitui por espaçoes"""
    var1 = str.split(frase)
    var2 = str.join(var1,' ')
    return var2