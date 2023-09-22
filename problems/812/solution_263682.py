def retira_pontuacao(frase):
    """Retire todas as pontuações da frase inicial e substitua por um espaço"""
    sinais="?,:;,."
    frase1 = frase1.replace(sinais," ")
    if sinais in sinais:
        return frase1