def busca(string,matriz):
    '''
    funcao que recebe uma matriz com os dados de 
    funcionarios de uma empresa e um setor, e retorna
    os dados do funcionario desse setor
    str,list - > list
    '''
    l = []
    i = 0
    for i in len(matriz):
    	if string in matriz[i]:
        	l.append(matriz[i])
    	i += 1
        
    return l