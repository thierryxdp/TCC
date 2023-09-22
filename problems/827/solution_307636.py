def qtd_divisores(numero):
    '''
    	Função que recebe um número
        e retorna quantos divisores 
        esse número tem
        : param numero: int
        : return: int
    '''
    possiveis_divisores = list(range(1,numero+1))
    divisores = []
    
    for elemento in possiveis_divisores:
        if numero%elemento == 0:
            list.append(divisores,elemento)
            
    return len(divisores)