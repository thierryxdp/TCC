def busca(setor, matriz):
    """ função que receber uma matriz e o nome do setor como argumento e retorna
    os dados de todos os funcionarios do setor """
    
    resultado = []
    for funcionario in matriz:
    	if setor in funcionario:
            copiaFuncionario = funcionario[:]
            list.remove(copiaFuncionario, setor)
            list.append(resultado, copiaFuncionario)
    return resultado