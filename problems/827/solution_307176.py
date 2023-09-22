def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
    soma=0

    for div in range(1, numero):
        if numero%div == 0:
            soma=soma+1
             
        return soma 
    else:
        return 0