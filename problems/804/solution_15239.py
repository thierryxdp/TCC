def filtra_pares(x):
    """Calcula uma função que recebe uma tupla com 4 numeros inteiros e retorna todos os valores pares pertencentes;
    tuple-->tuple"""
    a = x[0] 
    b = x[1] 
    c = x[2]
    d = x[3]
    tupla_final = ()
    if a%2==0:
        tupla_final=tupla_final + (a,)
    if b%2 == 0:
        tupla_final= tupla_final + (b,)
    if c % 2 == 0:
        tupla_final= tupla_final + (c,)
    if d % 2 ==0:
        tupla_final= tupla_final + (d,)

    return tupla_final