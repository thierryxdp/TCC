def primo(num):
    
    '''Função que dado um número,
    verifica se ele é primo ou não.
    Retorna True se for, e False se não.
    
    :param num: int
    :return: bool'''
    
    contador=1
   
    for i in range(2,num):
        if num%i==1:
            contador=contador+1
            return True
        
    else:
        return False