def retira_pontuacao(s):
    """retorna a frase de entrada sem sinais de pontuação"""
    for x in ",.:;!?-":
        frase = str.replace(s,x,' ')
        return frase