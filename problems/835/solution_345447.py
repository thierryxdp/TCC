def melhor_volta(m):
    '''função que, dada uma matriz,retorna uma tupla com 3 inteiros : piloto que efetuou
    a melhor volta, com qual tempo e em que volta; list -> tuple'''
    lista=[0,0]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] < m[lista[0]][lista[1]]:
                tempo = m[i][j]
                lista = [i,j]
                piloto = i+1
                volta = j+1
    return piloto,tempo,volta