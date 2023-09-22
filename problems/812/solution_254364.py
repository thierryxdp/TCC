def retira_pontuacao(s):
    """retorna a frase de entrada sem sinais de pontuação"""
    if "!" in s:
        return str.replace(s,"!"," ")
    elif "," in s:
        return str.replace(s,","," ")