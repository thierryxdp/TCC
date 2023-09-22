def qtd_divisores(numero):
    '''Função que conte quantos divisores tem um número, int -> int'''
    for elemento in range(1, numero//2+1):
        if numero%elemento == 0:
            return elemento