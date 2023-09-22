def qtd_divisores(n):
    '''Funcao que recebe de entrada um numero inteiro e 
    retorna QUANTOS divisores este numero posssui.
    int -> int'''
    divisores = 0
    for divisor in range(1,n+1): # uso n+1 pois um numero nunca vai ser divisivel por outro maior que ele
        if n % divisor == 0: #se o resto da divisao eh zero, esse num eh um divisor de n
            divisores = divisores + 1
    return divisores

# # TESTES
# qtd_divisores(27) == 4
# qtd_divisores(100) == 9
# qtd_divisores(1313) == 4