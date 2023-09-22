def retira_pontuacao(x):
    """retorna a frase de entrada com todas os caracteres de pontuação substituídos
por espaço"""
    return str.replace(x,"/",".",":",";","?","!",","," ")