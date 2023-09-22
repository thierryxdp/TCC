def qtd_divsores(num):
    '''
       Função que recebe um numero (num) e retorna a
       quantidade de divisores que esse numero tem;
       int -> int
    '''
    divisores=[]
    for i in list(range(num)):
        if i**10==1:
            divisores+=[i]
    return len(dividores)