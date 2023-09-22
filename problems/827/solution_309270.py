def qtd_divisores(numero):
    '''a funcao retorna quantos divisores o numero possui
    int->int'''
    for i in range(1,numero/2+1):
        if(numero%i)==0:
            divisores=i+1
            return divisores