def inverte(s):
    '''Retorna sua frase na ordem inversa de palavras.
    str -> str'''
    import string
    punct = string.punctuation
    for c in punct:
       s = s.replace(c, " ")
    s=str.split(s)
    s=s.reverse()
    return str.join(' ',str.split(s))