def lingua_p(s):
    """Dada uma string s, traduz ela para a língua do P, 
    que consiste em adicionar um p depois de cada vogal e
    repeti-la após o p"""
    a = []
    i = 0
    b = ''
    for e in s:
        a = a + [e]
    while i < len(a):
        if a[i] in 'AEIOUaeiou':
            a.insert(i+1,'p')
            a.insert(i+2,a[i])
        i = i + 1
	while i < len(a):
    	b.join(a[i])
        i = i + 1
    return b.lower