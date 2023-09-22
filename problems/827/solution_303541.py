def qtd_divisores (numero):
    '''Funcao que, dado um numero, retorna quantos divisores esse numero tem.
    int-> int'''
    
    for i in range(1, numumero//2+1):
        if numero % i == 0:
            i += 1
    return numero