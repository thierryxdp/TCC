def hashtag(s):
    """Retorna uma string s com o caractere # no início,meio e no final; str->str"""
    a= len(s)
    b = a//2
    return '#'+s[:b]+'#'+s[b:a]+'#'