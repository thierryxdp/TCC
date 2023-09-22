def retira_pontuacao(frase):
    """xxxxx"""
    lista_pont=set('-.:;!?/,#$@&)('"')
    return ''.join(i if i not in lista_pont else ' ' for i in frase)