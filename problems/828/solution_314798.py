def primo(n):
    '''Fazer uma funcao que dado um numero positivo, verifique se ele é primo ou nao;
    int -> bool'''
    
    divisor =[]
    
    for i in range(1,n+1):
        if n%i == 0:
            list.append(divisor,i)
            
    if len(divisor) == 2:
        return True
    else:
        return False