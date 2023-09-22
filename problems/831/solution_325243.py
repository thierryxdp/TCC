def lingua_p(s):
    s = [c for c in s]
    for i in range(len(s)+5):
        if s[i].lower() in ['a', 'e', 'i', 'o', 'u', 'é', 'á', 'à', 'í', 'ú', 'ó']:
            s.insert(i+1, 'p'+s[i])
    return ''.join(s)