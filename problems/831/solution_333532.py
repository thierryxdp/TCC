def lingua_p(palavra):
    c = 'a','e'
    lst = []
    for pos,char in enumerate(palavra):
        if(char == c):
            lst.append(pos)
    return lst