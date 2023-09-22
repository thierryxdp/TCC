def qtd_divisores(num):
    """conta quantos divisores um numero tem.
    int -> int"""
    lista = (range(1,100))
    divisores=[]
    for divi in lista:
        if num%divi==0:
            list.append(divisores,divi)
    return list.count(divisores)