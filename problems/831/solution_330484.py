def lingua_p(palavra):
    
    '''Função que dada uma frase, retorna a mesma
    na lingua do P
    
    :param palavra: str
    :return:str'''
    
    vogal='aeiouáéíóú'
    linguap=''
    
        
    for indice in range(len(palavra)):
        if palavra[indice] in vogal:
            linguap=linguap+palavra[indice]+'p'+palavra[indice]
            
        if palavra[indice] not in vogal:
            linguap=linguap+palavra[indice]
            
        
    return linguap