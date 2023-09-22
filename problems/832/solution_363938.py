def eh_quadrada(matriz):
    ''' funcao que verifica se uma matriz é ou  nao quadrada ou seja se esta ou nao vazia
    list-> bool'''
   
    for i in matriz[linhas][colunas]:
        if len (matriz[linha])== len(matriz[colunas]):
            return True
        if len(matriz[linha])!= len(matriz[colunas]):
            return False