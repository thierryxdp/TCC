def qtd_divisores (x):
    """conta quantos divisores o numero passsado como entrada tem;
    int -> int"""
    soma = 0
    for y in range (1,x+1):
        if x%y == 0:
            soma = soma + 1
    return soma