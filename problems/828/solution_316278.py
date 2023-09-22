def primo(num):
    
    '''Função que dado um número,
    verifica se ele é primo ou não.
    Retorna True se for, e False se não.
    
    :param num: int
    :return: bool'''
    
    contador=0
   
    for multip in range(2,num):
        if num%multip==0:
            contador=contador+1
            return False
        
    else:
        return True