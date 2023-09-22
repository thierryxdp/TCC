def busca(setor, matriz):
    '''Retorna os funcionários de um dado (setor)
    str, list -> list'''
    
    resultado = []
    
    for value in matriz:
        if value[2] == setor:
            value.remove(setor)
            resultado.append(value)
            
	return resultado