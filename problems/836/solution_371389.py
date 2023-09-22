def busca(setor, matriz):
    '''ao receber uma matriz com as colunas representando
    informações dos funcionários e um setor da empresa, 
    retorna todos os funcionários daquele setor.
    str, list -> list'''
    funcionarios = []
    for linha in matriz:
        for string in linha:
        	if string == setor:
                list.remove(linha, string)
            	list.append(funcionarios, linha)
    return funcionarios