def hashtag(s):
    """Função que recebe uma string e insere o caractere # no inicio,no meio e no final dela;str->str"""
    return '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'