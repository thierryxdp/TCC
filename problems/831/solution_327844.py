def lingua_p(string):
    a = string.find('a')
    e = string.find('e')
    i = string.find('i')
    o = string.find('o')
    u = string.find('u') 
    for i in string:
        if i in 'a':
            string.replace(a+1,p)
        if i in 'e':
            string.replace(e+1,p)
        if i in 'i':
            string.replace(i+1,p)
        if i in 'o':
            string.replace(o+1,p)
        if i in 'u':
            string.replace(u+1,p)
    return string