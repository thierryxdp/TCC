def lingua_p(s):
    """Dada uma string s, traduz ela para a língua do P, 
    que consiste em adicionar um p depois de cada vogal e
    repeti-la após o p"""
    a = []
    b = []
    i = 0
    c = ''
    for e in s:
        a = a + [e]
    while i < len(a):
        i = i + 1
        if a[i] in 'AEIOUaeiou':
            b.insert(i+1,'p')
            b.insert(i+2,a[i])
	while i < len(b):
    	c.join(b[i])
        i = i + 1
    return c.lower