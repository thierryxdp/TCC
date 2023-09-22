def uppCons(s):
    c=0
    i=''
    while c<len(s):
        if s[c] in 'bcdfghjklmnpqrstvxwyzBCDFGHJKLMNPQRSTVXWYZ':
            str.upper(s[c])
        i+=s[c]
    	c+=1
    return i