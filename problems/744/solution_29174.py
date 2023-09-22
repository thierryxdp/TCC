def hashtag(s):
    """retorna a string de entrada com o caractere no inicio, no meio e no final dela;
    string -> string"""
    metade=len(s)/2
    return '#'+s[0:metade]+'#'+s[metade+1:]+'#'