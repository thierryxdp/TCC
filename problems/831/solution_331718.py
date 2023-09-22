def lingua_p(s):
    '''
    	A função recebe uma string contendo uma palavra em português e traduz ela
        para a lígua do P. Na lígua do P toda vogal é seguida de p mais essa vogal.
        s -> str (palavra em portugês)
        str -> str
    '''
    s = s.lower
    s = list(s)
    for i in range(len(s)):
        if s[i] in 'aeiou':
            s[i] = s[i] + 'p' + s[i]
    str(s)
    return s