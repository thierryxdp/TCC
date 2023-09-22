def primo(numero):
    '''dado um numero inteiro positivo retorna se é primo ou nao'''
    '''int->bool'''
    
    divisores = []
    
    for i in range(1,numero+1):
        if numero%i ==0:
            list.append(divisores,i)
    
    if len(divisores) <= 2:
        return True
    else:
        return False