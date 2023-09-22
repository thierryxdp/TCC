def lingua_p(s):
    s.lower()
    lista=[]
    for c in range(len(s)):
        if s[c] in 'aeiou':
            lista=s.split()
            lista.pop(2)
            lista.insert(c,s[c]+'p'+s[c])
    return ''.join(lista)