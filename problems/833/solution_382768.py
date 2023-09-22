def conta_numero(numero,matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    qtd_n = 0
    
    if matriz == []:
        return 0
    for i in matriz:
        if str(numero) in str(matriz[linhas]):
        		qtd_n += str.count(str(matriz),str(numero))
    return qtd_n