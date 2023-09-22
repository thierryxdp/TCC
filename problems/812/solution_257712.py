def retira_pontuacao(frase):
    """retira a pntuação de uma frase; str->str"""
    frase= str.split(frase)
    pontos=[",","!","?","."]
    return frase- pontos[0]