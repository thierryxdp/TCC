def qtd_divisores(num):
    """conta quantos divisores um numero tem.
    int -> int"""
    lista = (range(1,100))
    divisores=[]
    if num<0:
        num=num*(-1)
    for divi in lista:
        if num%divi==0:
            list.append(divisores,divi)
    return len(divisores)