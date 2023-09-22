def lingua_p(string): 
    for i in string:
        if i in 'a':
            string.replace('a','p')
        if i in 'e':
            string.replace('e','p')
        if i in 'i':
            string.replace('i','p')
        if i in 'o':
            string.replace('o','p')
        if i in 'u':
            string.replace('u','p')
    return string