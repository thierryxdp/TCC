def lingua_p(palavra):
    '''Dada uma palavra, retorna essa mesma
    palavra na lingua do P'''
    i = 0
    indices = []
    for letra in palavra:
        if letra in 'aâãáeéiíoóuú':
        	letra = letra + 'p' + letra
   			indices.append(index(palavra))
   	traducao = palavra[::]
    
	return indices