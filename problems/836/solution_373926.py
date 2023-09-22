def busca(setor, matriz):
    '''Retorna os funcionários de um dado (setor)
    str, list -> list'''
    
    resultado = []
    
    for value in matriz:
        if value[2] == setor:
            resultado.append(value.remove(setor))
            
	return resultado