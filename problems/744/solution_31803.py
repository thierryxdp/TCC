def hashtag(s):
    """funçao que recebe uma string e adiciona # no inicio
    meio e fim de string
    str -> str"""
    a=len(s)//2
        return '#'+s[0:a]+'#'+s[a:]+'#'