def busca(setor,func):
    ''''''
    lin = len(func)
	col = len(func[0])
	l1 = []
if setor in func[0]:
    l1 = l1 + [func[0]]
    l1[0].remove('contabilidade')
    l1 = l1
if setor in func[1]:
    l1 = l1 + [func[1]]
    l1[1].remove('contabilidade')
if setor in func[2]:
    l1 = l1 + [func[2]]
    l1[1].remove('contabilidade')
return l1