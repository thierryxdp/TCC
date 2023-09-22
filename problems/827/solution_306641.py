def qtd_divisores(n):
    '''Função que retorna quantos divisores um número passado como
    	parâmetro possui
        
        in -> int'''
    
    divisores = 0
    for i in range(n+1):
        if i != 0 and n%i == 0:
            divisores = divisores + 1
    return divisores