def melhor_volta(matriz):
    ''' '''
    lista_min=[]
    for linha in range(len(matriz)): 
        minimo= min(matriz[linha])
        lista_min.append(minimo)
        minimo_final= min(lista_min)
    for linha in range(len(matriz)):        
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == minimo_final:
                return (linha+1,minimo_final,coluna+1)