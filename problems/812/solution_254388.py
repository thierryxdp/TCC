def retira_pontuacao(s):
    """retorna a frase de entrada sem sinais de pontuação"""
    s1 = s.replace("-"," ")
    s2 = s1.replace("."," ")
    s3 = s2.replace("!"," ")
    s4 = s3.replace("?"," ")
    s5 = s4.replace(":"," ")
    s6 = s5.replace(";"," ")
    s7 = s6.replace(","," ")
    return s7