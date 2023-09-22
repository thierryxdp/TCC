def lingua_p(palavra):
    c = 'a'
    lst = []
    for pos,char in enumerate(palavra):
        if(char == c):
            lst.append(pos)
        lst[c] = 'apa'
    return lst