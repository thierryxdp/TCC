def posLetra(string, ch,n):
    if string.rfind(ch)<n:
        return -1
    i = 0
    r=0
    while i < len(str):
        if str[i] == ch:
            r+=1
        i+=1
    return r