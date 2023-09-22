def soma_h(n):
    """
    Dado um valor, a função calculará a soma
    1+(1/2)+(1/3)+...+(1/valor) 
    int->float
    """
    lista=[]
    for i in range(1,n+1):
        H=1/i
        list.append(lista,H)
        resultado=sum(lista)
    return round(resultado,2)