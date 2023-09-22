def qtd_divisores(num):
    '''retorna a quantidade de divisores de um numero(num) dado.
    int --> int'''
    
    divisores = []
    for i in range(1,num+1):
        if num%i == 0:
            list.append(divisores, i)
        return len(divisores)