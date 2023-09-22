def conta_numero (numero,matriz):
    '''funcao que retorna quantas vezes aquele numero
    aparece na matriz'''
    '''int, list[lista] -> int'''
vezes = 0
for i in range(len(matriz)):
    for j in (matriz[i]):
        if j == numero:
            vezes = vezes+1
return vezes