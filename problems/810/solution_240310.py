def inverte(s):
    '''Retorna sua frase na ordem inversa de palavras.
    str -> str'''
    import string
    punct = string.punctuation
    for c in punct:
       s = s.replace(c, " ")
    s=str.split(s)
    i=0
    lista=[]
    while i<len(s):
        lista = lista + s[len(s)-i]
        i=i+1
    return str.join(' ',lista)