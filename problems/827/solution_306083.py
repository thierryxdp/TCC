def qtd_divisores(num):
    """funcao que conra o total de divisores de um numero"""
    """int->int"""
    div = []
    a=1
    for a in range(1,n+1):
        if num % a ==0:
            div.append(a)
    return len(div)