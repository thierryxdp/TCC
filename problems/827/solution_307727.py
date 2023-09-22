def qtd_divisores(num):
    '''
        Funcao recebe um numero inteiro e
        retorna quantos divisores esse numero tem.
        int -> int
        
    '''
    conta_divisores = 0
    
    for n_candidato in range(1,num+1):
        if num%n_candidato == 0:
            conta_divisores = conta_divisores + 1
    return conta_divisores