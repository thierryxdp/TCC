def qtd_divisores(num):
    """essa função recebe um número e determina quantos divisores ele possui;
    int->int"""
    numero = 0
    if num<0:
        return 0
    for i in range(1,int(num/2+1)):
        if num%i==0:
            numero+=1
    return numero + 1