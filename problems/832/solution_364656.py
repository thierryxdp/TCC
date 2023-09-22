def eh_quadrada(matriz_recebida):
    contador = 0
    contador_aux = 0
    matriz = []
    for i in matriz_recebida:
        linha = []
        for j in i:
            elemento = j
            linha.append(elemento)
            contador_aux += 1
        matriz.append(linha)
        contador+=1
        if contador^2 == contador_aux and contador^2 == 0 and contador^2 = '[]' :
            return True
        else:
            return False