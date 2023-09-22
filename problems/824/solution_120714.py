def uppCons(s):
    c=0
    while c<len(s):
        if s[c] in 'bcdfghjklmnpqrstvxwyzBCDFGHJKLMNPQRSTVXWYZ':
            str.upper(s[c])
    	c+=1
    return s