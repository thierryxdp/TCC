def qtd_divisores(num):
    """função que calcula o total de divisores de um numero
    int->int"""
    div=0
    for numero in range(1,num):
        if num%numero == 0:
            div=div+1
            
            
    return div