def lingua_p(palavra):
    c = 'aeiou'
    lst = []
    for pos,char in enumerate(palavra):
        if(char == c):
            lst.append(pos)
    return lst