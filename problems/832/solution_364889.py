def eh_quadrada(matriz):
    '''função que recebe uma matriz e verifica se ela é quadrada
    list->bool'''
    
    zeros=0
    qtd=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            qtd=qtd+1
            if matriz[i][j]==0:
                zeros=zeros+1
                
    if zeros==qtd:
        return True
    if zeros!=qtd:
        return False