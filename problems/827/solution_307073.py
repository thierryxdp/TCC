def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
    
    divisor=1
    qtd_divi=0
    while divisor <= numero:
        if numero%divisor ==0:
            qtd_divi=qtd_divi+1
            divisor=divisor+1
            
            return qtd_divi