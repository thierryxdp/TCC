def qtd_divisores(algarismo):
    '''
    Função que recebe um valor e retorna a quantidade de divisores
    que o mesmo possui.

    int -> int
    '''
    i = 1
    cont = 0
    
    while i <= algarismo:
        
        if algarismo%i == 0:
            cont += 1
            
        i += 1

    return cont