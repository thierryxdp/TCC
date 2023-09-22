def primo(num):
    '''Função que ao adicionar um numero inteiro e positivo,
    diz se ele é primo ou nao.
    int -> bool'''
    
    for x in range(2,num):
        
        if num % x ==0:
            return False
    
    else:
            return True