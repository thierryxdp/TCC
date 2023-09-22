def repetidos(h):
    c=0
    for i in range(len(h)):
        if h[i] == h[i-1]:
            c = c + 1
    return c