def hashtag(s):
    """retorna a string de entrada com o caractere no inicio, no meio e no final dela;
    string -> string"""
    return '#'+s[0:(len(s)/2)]+'#'+s[((len(s)/2)+1):]+'#'