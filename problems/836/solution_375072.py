def busca(setor, matriz):
    '''função que recebe uma matriz com dados de funcionários e um setor e retorna quais 
    funcionários fazem parte do setor passado como entrada.
    str, list -> list'''
    l = []
    for x in range(len(matriz)):
      #  for z in range(len(matriz[x])):
            if matriz[x][2] == setor:
                l += [[matriz[x][0]] + [matriz[x][1]] + [matriz[x][3]]]              
    return l