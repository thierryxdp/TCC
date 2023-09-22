def hashtag(s):
    """ função que, dada uma string s, retorne a mesma com o caractere '#'
        em seu início, meio e fim
        str -> str"""
    x=len(s)
    y=x//2
    z=y + x % 2
    parte1str=s[0:y]
    parte2str=s[y:x]
    return '#' + parte1str + '#' + parte2str + '#"