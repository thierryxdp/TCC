def eh_quadrada(matriz):
    """funcao que retorna se a matriz e quadrada ou nao;
    list(list) -> bool"""
    l = []
    c = []
    lin = 0
    col = 0

    for i in matriz:
        lin+=1
        l.append(lin)
        
        
        for j in matriz[l]:
            col+=1
            c.append(col)
            

    if len(l)==1 and len(c)==1:
        return False
    
    if len(l) == len(c):
        return True

    else:
        return False