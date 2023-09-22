def eh_quadrada(matriz):
    """funcao que retorna se a matriz eh quadrada ou nao;
    list(list) -> bool"""
    
    c=0
    l=0

    for i in range(len(matriz)):
        l+=1
        for j in range(len(matriz[i])):
            c+=1

    if l==0 and c==0:
        return True
    
    if l == c//l:
        return True

    else:
        return False