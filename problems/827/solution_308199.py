def qtd_divisores(num):
    
    '''Função que dado um número,
    retorna quantos divisores o mesmo tem.
    
    :param num: int
    :return:int'''
    
    contador=1
    
    for x in range(1,num):
        if num%x==0:
            contador=contador+1
            
    if num<0:
        return 0
            
    return contador