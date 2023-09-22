def retira_pontuacao(frase):
    """Retire todas as pontuações da frase inicial e substitua por um espaço"""
    sinais="?,:;,."
    for sinais in sinais:
        frase1 = frase1.replace(sinais," ")
        return frase1