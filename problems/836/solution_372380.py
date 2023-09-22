def busca(setor,funcionarios):
    """
    Função recebe uma matriz(funcionarios) com os dados dos funcionarios e um 
    setor da empresa(setor). Retorna os dados dos funcionários que participam do 
    determinado setor escolhido.
    str, matriz -> matriz
    """
    funcionariosetor=[]
    for i in range(len(funcionarios)):
        if funcionarios[i][2]==setor:
            del funcionarios[i][2]
        	list.append(funcionariosetor,funcionarios[i])
           
  	
    return funcionariosetor