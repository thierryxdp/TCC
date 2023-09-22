def hashtag(s):
    """retorna a string de entrada com o caractere no inicio, no meio e no final dela;
    string -> string"""
    quant_total=len(s)//2
    return '#'+s[0:quant_total]+'#'+s[(quant_total)+1:]+'#'