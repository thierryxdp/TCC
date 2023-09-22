def melhor_volta(m):
    [[1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10],
     [1,2,3,4,5,6,7,8,9,10]]
    a = 100000000 #maior numero possivel
    for i in range(len(m))#[1,2,3,4,5,6]:
        for j in range(len(m[i]))#[1,2,3,4,5,6,7,8,9,10]:
            if m[i][j]  < a : # sentença que compara se o numero atual é menor que o menor numero armazenado
                a = m[i][j]	  #caso for, ele anota todas as caracteristicas daquele tempo, como o piloto
                melhorPiloto = i + 1# , numero da volta e armazena o novo menor numero como parametro pras proximas comparações
                nVolta = j + 1
                melhorVolta = a
          
	return (melhorPiloto, melhorVolta, nVolta)