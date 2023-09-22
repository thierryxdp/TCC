def qtd_divisores(num):
    '''Recebe um número e retorna a quantidade 
    de divisores que nele existe
    int->int'''
    qtd_div=0
    for i in range(1,num+1):
        if num%i==0:
            qtd_div=qtd_div+1
    return qtd_div