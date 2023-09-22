def soma_h(num_inteiro):
    '''
    função que recebe um numero inteiro N e retorna o resultado, 
    com 2 casas decimais, de H com N termos
    int -> int
    '''
    
    soma_H = 0
    for k in range(1, num_inteiro + 1):
        fracao_pa = (1/k)
        soma_H=soma_H+fracao_pa
    return round(soma_H, 2)