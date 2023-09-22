def qtd_divisores(x):
    """retorna a quantidade de divisores de um número
    int->int"""
    lista=[]
    if x<0:
        return 0
    for n in range(x):
        if n==0:
            lista=[]
        else:
            if x%n==0:
                list.append(lista,n)
    lista1=len(lista)+1
    return lista1