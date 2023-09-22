def busca(setor,matrizfuncionarios):
    ''' funcao que dado uma matriz com dados dos funcionarios retorne somente os funcionarios que fazem parte do setor
    str,list->'''
    funcionarios= []
    for i in range(len(matrizfuncionarios)):
		if setor == matrizfuncionarios[i][2]:
			del matrizfuncionarios[i][2]
			funcionarios += [matrizfuncionarios[i]]                
    return funcionarios