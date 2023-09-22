def ehquadrada(matriz): 
    a = len(matriz[0]) #linhas
    zero = len(matriz[0])
    if zero==0:
        return True  
    if  a == 0:
        return True
    b = len(matriz[0][0]) #colunas
    #há uma limitação da lista caso seja criada uma com só uma linha, não como verificar o numero de colunas
    if a==b:
        return a==b
    else:
        return a==b