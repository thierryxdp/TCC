def qtd_divisores(numero):
    '''recebe um numero inteiro e conta quantos divisores
    esse numero tem
    int -> list'''
    
    divisores = []
    
    for i in range(1,numero + 1):
        if numero%i == 0:
            list.append(divisores, i)
    return len(divisores)