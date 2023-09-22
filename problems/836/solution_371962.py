def busca(setor,func):
	''' dada uma matriz faz uma busca por setor dado um nome de um setor da empresa e retorna os dados de todos os funcionarios daqueles setor'''
    lin= len(func)
    col=len(func[0])
    l1=[]
    if setor in func[0]:
        l1=l1+[func[0]]
        l1[0].remove(setor)
        l1=l1
	if setor in func[1]:
        l1=l1+[func[1]]
        l1[0].remove(setor)
	if setor in func[2]:
        l1=l1+[func[2]]
        l1[1].remove(setor)
    return l1