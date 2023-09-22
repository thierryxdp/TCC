def primo(numero):
    '''recebe um numero inteiro positivo e retorna True
    se ele for primo e False se não for primo
    int -> bool'''
    
    divisores = []
    
    for i in range(1,numero+1):
        if numero%i == 0:
            list.append(divisores,i)
    if len(divisores) == 2:
        return True
    else:
        return False