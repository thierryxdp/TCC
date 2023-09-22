def fatorial(num):
    '''Função que calcula o fatorial do número fornecido
    int -> int
    '''
    resposta = 1
    while num>1:
        resposta = resposta * (num)
        num -=1
    return resposta