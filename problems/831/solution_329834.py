def lingua_p(s):
    """Dada uma string s, traduz ela para a língua do P, 
    que consiste em adicionar um p depois de cada vogal e
    repeti-la após o p"""
    a = []
    b = []
    i = 0
    c = ''
    x = 0
    for e in s:
        a = a + [e]
    while i < len(a):
        if a[i] in 'AEIOUaeiou':
            list.insert(b,i + 2*x,a[1])
            list.insert(b,i+1 + 2*x,'p')
            list.insert(b,i+2 + 2*x,a[i])
            x = x + 1
        if a[i] not in 'AEIOUaeiou':
            list.insert(b,i + 2*x,a[i])
        i = i + 1
	while i < len(b):
    	c.join(b[i])
        i = i + 1
    return c.lower