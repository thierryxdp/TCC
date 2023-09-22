def busca(setor, m):
    '''
    Dada uma matriz com funcionarios devolve as informacoes de 
    funcionarios de determinado setor.
    
    Entrada/Saida:
    string, list -> list
    '''
    registro = []
    for i in m:
        if i[2] == setor:
            del i[2]
            registro.append(i)
	return registro