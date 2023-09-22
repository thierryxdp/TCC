def filtra_pares(x):
    """Recebe uma tupla com quatro elementos inteiros como entrada e retorna
       uma nova tupla contendo apenas os elementos paresda tupla original
       parãmetro de entrada: tipo tupla
       parâmetro de saída: tipo tupla"""
    n_pares=()
    if (x[0]%2==0) and (x[1]%2==0) and (x[2]%2==0) and (x[3]%2==0):
        return n_pares+(x[0],x[1],x[2],x[3])
    elif (x[0]%2==0) and (x[1]%2==0) and (x[2]%2==0):
        return n_pares+(x[0],x[1],x[2])
    elif (x[0]%2==0) and (x[1]%2==0):
        return n_pares+(x[0],x[1])
    elif (x[1]%2==0) and (x[2]%2==0) and (x[3]%2==0):
        return n_pares+(x[1],x[2],x[3])
    elif (x[2]%2==0) and (x[3]%2==0):
        return n_pares+(x[2],x[3])
    elif (x[0]%2==0):
        return n_pares+(x[0])
    elif (x[1])%2==0):
        return n_pares+(x[1])
    elif (x[2]%2==0):
        return n_pares+(x[2])
    elif (x[3]%2==0):
        return n_pares+(x[3])
    else:
        return n_pares