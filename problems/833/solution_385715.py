def conta_numero(inteiro,matriz):
    "Função que conta e retorna quantas vezes um inteiro aparece em uma matriz. int, list --> int"
    qtd=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j==inteiro:
                qtd+=1
    return qtd