def qtd_divisores(n):
    '''função que conta quantos divisores um dado numero tem
    int -> int'''
    resposta = 0
    for x in range(n):
        num = 1
        if n%num==0:
            resposta = resposta + 1
        numa = num + 1
        
    return resposta