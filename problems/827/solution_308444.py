def qtd_divisores(n):
    '''função que conta quantos divisores um dado numero tem
    int -> int'''
    resposta = 0
    num = 1
    for x in range(n):
        if n%num==0:
            resposta = resposta + 1
        num = num + 1
        
    return resposta