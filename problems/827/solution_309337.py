def qtd_divisores(n):
    '''
    Funçao que conta a quantidade de divisores de um numero
    int->int
    '''
    qtd=[1,n]
    for i in range(2,n):
        if n == 0 or n<0:
            list.clear(qtd)
        elif n%i == 0:
            list.append(qtd,i)
            
    return len(qtd)