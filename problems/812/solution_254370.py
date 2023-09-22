def retira_pontuacao(s):
    """retorna a frase de entrada sem sinais de pontuação"""
    x = (",",".","!","?","-",":",";")
    for x in s:
        return str.replace(s,x," ")