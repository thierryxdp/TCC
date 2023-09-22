#Buscando na Matriz
def conta_numero(numero, matriz):
    #Função retorna quantas vezes aquele número aparece na matriz; Int,List =>int
    quantidade = 0
    for i in range(len(matriz)):
         quantidade += matriz[i].count(numero)
    return quantidade