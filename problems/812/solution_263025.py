def retira_pontuacao (frase, substring=('.' , '!' , '?' , '...' , ';' , ',' , ':' , '-' , '_')):
    """Dada a frase de entrada, retorna a frase sem os sinais de pontuação. str -> str"""
    substring = str(' ')
    return str.strip(str (frase), str (substring))