# A função recebe uma string e insere '#' no início, meio e fim da string.
# s:string
# str-> str
def hashtag(s):
    metade= len(s)/2
    return '#' + s[0:metade ] + '#' + s[metade+1:] + '#'