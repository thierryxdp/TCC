def qtd_divisores (x):
    """conta quantos divisores o numero passsado como entrada tem;
    int -> int"""
    soma = 0
    for y in range (x+1):
        if y!= 0 and x/y == 0:
            soma = soma + 1
    return soma