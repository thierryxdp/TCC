def qtd_divisores(n):
    """Dado um número n, a função retorna a quantidade de divisores que esse número possui;
    int-> int->"""
    lista=[]
    for num in range(1,n+1):
        if n%num==0:
            list.append(lista,num)
    quant_divisores=len(lista)
    return quant_divisores