def lingua_p(s):
    s = [c for c in s]
    v = ['a', 'e', 'i', 'o', 'u', 'é', 'á', 'à', 'í', 'ú', 'ó']
    for i in range(len(s)):
        if s[i].lower() in v:
            s[i] = s[i] + 'p' + s[i]
    return ''.join(s)