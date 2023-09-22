def eh_quadrada(matriz): 
    a = len(matriz) #linhas
    if  a == 0:
        return True
    b = len(matriz[0]) #colunas
    #há uma limitação da lista caso seja criada uma com só uma linha, não como verificar o numero de colunas
    if a==b:
        return a==b
    else:
        return a==b