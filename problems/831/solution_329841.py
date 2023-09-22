def lingua_p(s):
    """Dada uma string s, traduz ela para a língua do P, 
    que consiste em adicionar um p depois de cada vogal e
    repeti-la após o p"""
    p = s.lower()
    a = []
    b = []
    i = 0
    i1 = 0
    c = ''
    x = 0
    for e in p:
        a = a + [e]
    while i < len(a):
        if a[i] in 'AEIOUaeiou':
            list.insert(b,i + 2*x,a[i])
            list.insert(b,i+1 + 2*x,'p')
            list.insert(b,i+2 + 2*x,a[i])
            x = x + 1
        if a[i] not in 'AEIOUaeiou':
            list.insert(b,i + 2*x,a[i])
        i = i + 1
	while i1 < len(b):
    	c = c + b[i1]
        i1 = i1 + 1
    return c