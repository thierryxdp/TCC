def retira_pontuacao (frase):
    """Dada a frase de entrada, retorna a frase sem os sinais de pontuação. str -> str"""
    substring = ('.' , '!' , '?' , '...' , ';' , ',' , ':' , '-' , '_')
    return str.strip(frase, substring, ' ')