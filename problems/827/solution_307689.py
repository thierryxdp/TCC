def qtd_divisores(num):
    '''Função que conta quantos divisores o número dado pelo
       usuario tem.
       : param num: int
       : return: int
    '''
    lista_divisores=[]
    for el in range(1,num+1):
        if num%el==0: 
            lista_divisores.append(el)
    return len(lista_divisores)