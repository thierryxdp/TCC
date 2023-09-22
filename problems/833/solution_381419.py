conta_numero(numero,matriz):
    ''' funcao que dado uma matriz e um numero
    retorna quntas vezes esse numero aparece
    na matriz; list,int -> int'''
    
    qtd = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for i in range(linhas):
        for j in range(colunas):
            if i == numero:
                qtd = qtd + 1
    return qtd