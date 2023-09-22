def qtd_divisores(n):
    """conta qunatos divisores um número tem;int->int"""
    lista=list(range(1,n+1))
    resposta=[]
    
    for numero in lista:
        if (n%numero==0):
            list.append(resposta,numero)
    return lista