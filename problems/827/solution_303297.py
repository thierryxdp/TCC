def qtd_divisores(n):
    """coment"""
    lista_divisores=[]
    for num in range(1,n+1):
        if n%num==0:
            lista_divisores.append(num)
    return lista_divisores