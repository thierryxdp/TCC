def repetidos(n):
    i = 0
    rep = 0
    while i < len(n):
        if n[i] == n[i-1]:
            rep = rep + 1
        i = i + 1
    return rep