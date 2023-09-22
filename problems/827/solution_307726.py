def qtd_divisores(numero):
    '''retorna a quantidade de divisores de um número
    entrada= int
    saida=int'''
    h=[]
    for x in list(range(1,numero+1)):
        if numero % x == 0:
            list.append(h,x)
    return len(h)