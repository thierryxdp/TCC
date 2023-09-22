def retira_pontuacao (frase):
    """Função que dada uma frase, a retorne sem as pontuações e com um espaço no lugar"""
for char in "-,:;.!?":
        x = frase.replace(char, " ")
        return x