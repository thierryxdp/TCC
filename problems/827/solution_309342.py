def qtd_divisores(n):
    '''
    Funçao que conta a quantidade de divisores de um numero
    int->int
    '''
    qtd=[]
    for i in range(2,n):
        if n%i == 0:
            list.append(qtd,i)
    return len(qtd)