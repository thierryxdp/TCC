def lingua_p(palavra):
    c = 'a','e','i','o','u'
    lst = []
    for pos,char in enumerate(palavra):
        if(char == c):
            lst.append(pos)