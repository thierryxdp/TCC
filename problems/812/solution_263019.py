def retira_pontuacao (frase, substring):
    """Dada a frase de entrada, retorna a frase sem os sinais de pontuação. str -> str"""
    str (substring) = ('.' , '!' , '?' , '...' , ';' , ',' , ':' , '-' , '_')
    return str.strip(frase, substring, ' ')