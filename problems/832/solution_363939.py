def eh_quadrada(matriz):
    ''' funcao que verifica se uma matriz é ou  nao quadrada ou seja se esta ou nao vazia
    list-> bool'''
   
    for i in matriz[j][k]:
        if len (matriz[j])== len(matriz[k]):
            return True
        if len(matriz[j])!= len(matriz[k]):
            return False