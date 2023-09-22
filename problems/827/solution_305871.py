def qtd_divisores(n):
    """cria uma lista com todos os divisores de dado número e depois conta essa lista.int->int"""
    listadediv=[]
    for x in range(1,n+1):
        if n%x==0:
            list.append(listadediv,x)
    return len(listadediv)