def lingua_p(s):
    s.lower()
    lista=[]
    for c in range(len(s)):
        if s[c] in 'aeiou':
            lista=s.split(s[c])
            lista2=lista[:]
            lista2.pop(1)
            lista2.insert(c,s[c]+'p'+s[c])
    return ''.join(lista)