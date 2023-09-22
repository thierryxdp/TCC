def hashtag(s):
    """retorna uma string de entrada que recebe o caractere (#) no inicio, no meio eno final dela;
    string->string"""
    return '#'+s[0:(len(s)//2)]+'#'+s[(len(s)//2):]+'#'