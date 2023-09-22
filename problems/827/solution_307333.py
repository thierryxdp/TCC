qtd_divisores(num):
    """função que calcula o total de divisores de um numero
    int->int"""
    div=[]
    for numero in range(num):
        if numero%num ==0:
            list.append(div,numero)
            
    return len(div)