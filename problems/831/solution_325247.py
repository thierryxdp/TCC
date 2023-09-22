def lingua_p(s):
    s = [c for c in s]
    for i in range(len(s)+1):
        if s[i].lower() in ['a', 'e', 'i', 'o', 'u', 'é', 'á', 'à', 'í', 'ú', 'ó']:
            s[i] = s[i] + 'p' + s[i]
    return ''.join(s)