def qtd_divisores(numero):
    '''Função que retorna quantos divisores o numero tem;
	int -> int'''
    n=0
    for elemento in range(numero+1):
        if numero%elemento==0:
            n=n+1
    return n