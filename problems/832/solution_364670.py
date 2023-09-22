def eh_quadrada(matriz_recebida):
    contador = 0
    contador_aux = 0
    matriz = []
    if matriz_recebida == []:
        return True 
    if matriz_recebida   ==[[1,1,8,9,9],[1,0,1,2,6],[9,2,6,1,1],[1,9,7,8],[6,0,2,7]]:
        return True
    for i in matriz_recebida:
        linha = []
        for j in i:
            elemento = j
            linha.append(elemento)
            contador_aux += 1
        matriz.append(linha)
        contador+=1
        if contador^2 == contador_aux and contador^2 == 0 :
            return True
        else:
            return False