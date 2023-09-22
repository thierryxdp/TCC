def busca(set,mat):
    """Retorna as informacoes dos funcionarios de um dado setor
	entrada:
    	set, mat -> str, list
    saida:
    	list
	"""

    func=[]

    for lin in mat:
        for i in lin:
            if i==set:
                lin.remove(set)
                func = func + [lin]
    return func