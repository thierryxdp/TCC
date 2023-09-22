def inverte(s):
    '''Retorna sua frase na ordem inversa de palavras.
    str -> str'''
    import string
    punct = string.punctuation
    for c in punct:
       s = s.replace(c, " ")
    s=str.split(s)
    i=1
    lista=[]
    while i<len(s):
        list.append(lista,s[len(s)-1]
        i=i+1
    return str.join(' ',lista)