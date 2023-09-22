def primo(numero):
    '''Dado um número, a função deve retornar True se for 
    um número primo, e False se não for número primo;
    int ->bool'''
    
    for i in range(2,numero):
        if (numero%i==0):
            return False
        
    return True