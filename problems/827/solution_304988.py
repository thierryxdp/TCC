def qtd_divisores(n):
    '''Função que recebe um inteiro, verifica e retorna a quantidade
    de números capazes de dividi-lo.'''
    '''int -> int'''
    i = 0
    cont = 0
    for i in (1,n):
        if (n%i == 0):
            i += 1
        	cont += 1
    return cont