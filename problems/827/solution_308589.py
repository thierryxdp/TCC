def qtd_divisores(numero):
    '''Função que retorna quantos divisores o numero tem;
    int -> int'''
    n=1
    for elemento in range(1,numero//2+1):
        if numero%elemento==0:
            n=n+1
    if numero<=0:
    	return 0
    return n