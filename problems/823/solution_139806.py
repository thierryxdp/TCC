def faltante(n):
    i = 1
    r = []
    s = []
    while i <= len(n):
        if n[i] == n[i-1] + 1:
            r.append(n[i])
        elif n[i] != n[i-1] + 1:
            s.append(n[i])
    i = i + 1
    return s[0] - 1