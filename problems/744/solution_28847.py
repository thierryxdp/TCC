# A função recebe uma string e insere '#' no início, meio e fim da string.
# s:string
# str-> str
def hashtag(s):
    return '#' + s[0:s/2] + '#' + s[s/2+1:]