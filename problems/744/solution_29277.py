def hashtag(s):
    '''retorna uma string com '#' no meio
    str-->str'''
    numero= len(s)
     palavra = "#" + s[:numero//2] + "#" + s[numero//2:] + "#"
    return palavra