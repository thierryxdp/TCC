def primo(num):
    ''' dado um numero positivo(num), retorna um valor booleano dizendo se o numero é 
    primo ou não.
    int --> bool'''
    #usei a funcao criada para a qtd_divisores como base inicial
    
    divisores = []
    for i in range(1,num+1):
        if num%i == 0:
            list.append(divisores, i)
    if (num and 1 in divisores) and (len(divisores)==2):
        return True
    else:
        return False