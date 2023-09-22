def retira_pontuacao(frase):
    """ Define uma função que remove caracteres de pontuação """
    pontuacao = set('-.;:!?/\\,#@$&)(\'"')
    return ''.join(i if i not in pontuacao else ' ' for i in frase)