def hashtag(s):
    """dado uma string s, insere o caractere # no seu
    inicio, meio e fim
    str -> str"""
    meio=len(s)//2
    return "#" + s[0:meio] + "#" + [meio:] + "#"