def hashtag(s):
    """dada uma string s, insere o caractere 
    '#' no inicio, no meio e no final dela;
    string->string"""
    x=s
    return '#'+x[0:(len(s))//2]+'#'+x[(len(s))//2:]+'#'