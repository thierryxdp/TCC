def uppCons(s):
    c=0
    i=''
    while c<len(s):
        if s[c] in 'bcdfghjklmnpqrstvxwyzBCDFGHJKLMNPQRSTVXWYZ':
            i+=str.upper(s[c])
        else:
            i+=s[c]
    	c+=1
    return i