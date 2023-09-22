def eh_quadrada(m):
    
    """
    list--->bool
    Checa primeiro se a entrada é uma lista vazia(ou seja,matriz vazia).
    Após isso, checa se a quantidade de linhas é a mesma da de colunas, onde
    caso uma das 2 condicoes seja atendida, há o retorno de True e caso
    contrário,False
    """
    
    if list(m)==[]:
        return True
    if (len(m)==len(m[0])):
        return True
    else:
        return False