def posLetra(palavra, char, qnt):
	'''
    Verifica a posicao da ocorrencia numero qnt de um caracter char
    numa palavra, caso nao haja, retorna -1.
    
    Entrada/Saida:
    string, string, int -> int
    '''
    
    if palavra.count(char) >= qnt:
        i, ocur = 0, 0    
        while ocur < qnt:
            if palavra[i] == char:
                ocur += 1
			i += 1
		return i - 1
	
    return -1