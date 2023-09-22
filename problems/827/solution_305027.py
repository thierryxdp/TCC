def qtd_divisores(num):
    '''Função que dada um número(num) retorna a quantidade de
    divisores que ele possui
    int->int'''
    
    resultado=0
    
    for i in range(1,num+1):
        if num % i==0:
            resultado=resultado+1
    return resultado