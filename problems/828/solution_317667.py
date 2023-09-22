def primo(num_analisar):
    '''
    Funcao que retorna o resultado de uma analise se um numero inserido é primo
    int -> bool
    '''
    if num_analisar < 2:
        return False
    else:
        for n in range(2, num_analisar):
            if num_analisar % n == 0:
                return False
        return True