def hashtag(s):
    """Esta é a função que dada uma string retorna a mesma com uma hashtag no seu início,meio e fim,str->str"""
    x=len(s)//2
    a=s[:x]
    b=s[x:]
    return '#'+a+'#'+b+'#'