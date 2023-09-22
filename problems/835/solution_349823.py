def melhor_volta(m):
    '''Retorna o a melhor volta corredor em qual tempo e volta.
    list -> tuple''' 
    corredor = 1
    tempo = m[0][0]
    volta = 1
    for i in range(len(m)):
        for j in range(len(m[i])):
            if min(i) <= tempo:
                tempo = min(i)
                volta = i + 1
                corredor = j + 1
 	return (corredor, tempo, volta)