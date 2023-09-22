def retira_pontuacao(s):
    """retorna a frase de entrada sem sinais de pontuação"""
    s=str.split(s)
    return str.replace(s,"/,;:!?."," ")