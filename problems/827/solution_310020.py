def qtd_divisores(numero):
    r = 0
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20]
    for x in lista:
        if numero%x==0:
            r = r+1
    return x