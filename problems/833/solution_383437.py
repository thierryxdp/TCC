def conta_numero(numero, matriz):
    contador = 0
    for i in range(len(matriz)):
        for n in range(len(matriz[i])):
            if numero == matriz[i][n]:
            	contador+=1
    return contador

#Percorremos todos os indices da matriz usando um for e verificamos se é igual ao 
# numero passado como argumento, e caso sim, incrementamos um contador passado que é
# retornado no fim da função.