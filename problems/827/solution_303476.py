def qtd_divisores(n):
    '''Função que, dado um número inteiro n, conte quantos divisores ele tem
    int -> int
    '''
    divisores = [n]
    for a in range(n//2):
        if n%(range(1,n//2+1)[a])==0:
            list.append(divisores,range(1,n//2+1)[a])
    if n<0:
        resposta = 0
    else:
        resposta = len(divisores)
    return resposta