def posLetra(string, ch,n):
    if string.rfind(ch)<n:
        return -1
    i = 0
    r=0
    while i < len(string):
        if string[i] == ch:
            r+=1
        i+=1
    return r