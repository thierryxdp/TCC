def qtd_divisores(numero):
    '''a funcao retorna quantos divisores o numero possui
    int->int'''
    for i in range(1,numero+1):
        if(n%i)==0:
            divisores=i+1
            return divisores