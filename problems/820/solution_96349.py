def posLetra(texto,letra,numero):
    """Retorna a posição da string naquela ocorrência onde a letra está
    string, string, int --> int"""
    i = 0
    ocorrencia = 0
    
    while i < len(texto):
    
    	if texto[i] == letra:
        	ocorrencia =+ 1
        	if ocorrencia == numero:
                return i
		i += 1
        
    return -1