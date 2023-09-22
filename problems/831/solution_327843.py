def lingua_p(string):
    a = string.index('a')
    e = string.index('e')
    i = string.index('i')
    u = string.index('u') 
    for i in string:
        if i in 'a':
            string.replace(a+1,p)
        if i in 'e':
            string.replace(e+1,p)
        if i in 'i':
            string.replace(i+1,p)
        if i in 'u':
            string.replace(u+1,p)
    return string