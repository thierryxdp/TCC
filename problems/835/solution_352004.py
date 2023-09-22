def melhor_volta(m):
    a = 100000000 #maior numero possivel
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]  < a : # sentença que compara se o numero atual é menor que o menor numero armazenado
                a = m[i][j]	  #caso for, ele anota todas as caracteristicas daquele tempo, como o piloto
                melhorPiloto = i + 1# , numero da volta e armazena o novo menor numero como parametro pras proximas comparações
                nVolta = j + 1
                melhorVolta = a
          
	return (melhorPiloto, melhorVolta, nVolta)