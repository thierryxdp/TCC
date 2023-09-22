def primo(num):
    '''
        Funcao que recebe um numero inteiro positivo
        e retorna True se ele for primo e False caso
        contrario.
        int -> bool
        
    '''
    for menor_q_num in range(2,num):
        if menor_q_num%num == 0:
            return False
    return True