def repetidos(lis):
    i = 1
    rep = 0
    while(i<len(lis)):
        if(lis[i] == lis[i-1]):
            rep += 1
            i += 1
        else:
            i += 1
    return rep