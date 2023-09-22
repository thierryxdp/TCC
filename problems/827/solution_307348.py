def qtd_divisores(num):
    """função que calcula o total de divisores de um numero
    int->int"""
    div=[]
    for numero in range(1,num):
        if num%numero == 0:
            list.insert(div,numero)
            
            
    return div