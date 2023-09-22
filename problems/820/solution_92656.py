def posLetra(palavra, char, qnt):
    
    if palavra.count(char) >= qnt:
        i, ocur = 0, 0    
        while ocur < qnt:
            if palavra[i] == char:
                ocur += 1
			i += 1
		return i
	else:
        return -1