def retira_pontuacao(frase):
    """ Retira todas as pontuações do texto e as substitui por espaçoes"""
    var1 = str.split(frase)
    return str.join(var1,' ')