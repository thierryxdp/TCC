def posLetra(str, ch,n):
    i = 0
    while i < len(str):
        if str[i] == ch:
            return i
        i = i + 1
    return -1