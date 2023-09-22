def primo(num):
    
    '''Função que dado um número,
    verifica se ele é primo ou não.
    Retorna True se for, e False se não.
    
    :param num: int
    :return: bool'''
    
    contador=1
   
    for contador in range(1,num):
        if num%2==1:
            contador=contador+1
            return True
        
    else:
        return False