def conta_numero(numero,matriz):
    '''Retorna a quantidade de vezes que um número aparece
    na matriz;recebe como parâmetro o número e a matriz dado
    pelo usuário; int,list(list)-->int'''
    linha=len(matriz)
    coluna=len(matriz[0])
    conta=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero==matriz[i][j]:
                       conta+=1
    return conta