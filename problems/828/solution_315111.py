def primo(numero):
    '''dado um numero inteiro positivo retorna se é primo ou nao'''
    '''int->bool'''
    
    divisores = []
    
    for i in range(i,numero):
        if i%2==0:
            list.append(divisores,i)
    
    if len(divisores) <= 2:
        return True
    else:
        return False