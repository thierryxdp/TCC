def inverte(s):
    '''Retorna sua frase na ordem inversa de palavras.
    str -> str'''
    import string
    punct = string.punctuation
    for c in punct:
       s = s.replace(c, " ")
    s=str.split(s)
    i=0
    list() =()
    while i<len(s):
        list() = list() + s(len(s)-1)
        i=i+1
    return str.join(' ',list)