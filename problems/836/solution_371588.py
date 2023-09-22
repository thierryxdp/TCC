def busca(area,func):
    ''''''
    lin = len(func)
	col = len(func[0])
	l1 = []
	if 'contabilidade' in func[0]:
    	l1 = l1 + func[0]
	if 'contabilidade' in func[1]:
    	l1 = l1 + func[1]
	if 'contabilidade' in func[2]:
    	l1 = l1 + func[2]
	return l1