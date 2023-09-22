def fatorial(num):
    '''Dado um número inteiro, retorna o fatorial deste
    número.
    int -> int'''
    
    i = 0
    resposta = 1
    Num = num
    if num == 0 or num == 1:
        return 1
    else:
        while i < num:
            resposta = resposta*Num
            Num = Num - 1
            i = i + 1
        return resposta