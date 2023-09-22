def hashtag(s):
    """retorna s com o caractere # em seu inicio, meio e fim.
    str-> str"""
    x=len(s)//2
    inicio=s[:x]
    fim=s[x:]
    return '#'+inicio+'#'+fim+'#'