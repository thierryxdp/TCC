def melhor_volta(m):
    '''[[1,2,3,4,5,6,7,8,9,10],
    	[1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10]]	'''
    menoresVoltas = []
    for i in range(len(m)):
        linha = []
        minVolta = 0
        
        for j in range(len(m[i])):
        	a = m[i][j]
            list.append(linha ,a)
            if a <= m[i][j]:
                melhorPiloto = i + 1
                nVolta = j + 1
                melhorVolta = a
                
	return (melhorPiloto, melhorVolta, nVolta)                
            
    melhorTempo = min(menoresVoltas)
    melhorPiloto = 1 + list.index(menoresVoltas, melhorTempo)
    
            
    tupla = (melhorPiloto , melhorTempo)
    return tupla