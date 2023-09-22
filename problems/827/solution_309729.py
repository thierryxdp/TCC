def qtd_divisores(num_entrada):
    '''
    Funcao que retorna a quantidade de divisores de um numero
    após tal numero ser inserido na entrada da funcao
    int -> int
    '''
    divisores_numero = 0
    for num in range(1, (num_entrada + 1)):
        if num_entrada % num == 0 and num_entrada > 0:
            divisores_numero = divisores_numero + 1
    return divisores_numero