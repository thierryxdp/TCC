def maiores(lista,n):
    """retorna os números da lista que são maiores que n;
    strin, int-> string"""
    l= lista
    a= [x for x in l if x > n]
    b= a.sort()
    return a