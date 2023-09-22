def uppCons(frase:str)->str:
    
    """ Função que recebe como entrada uma frase qualquer e retorna a mesma frase 
   		com todas as consoantes maiúsculas.
        
    """
    
    cont = 0
    nova_frase = frase 
    vogais = ["a", "e", "i", "o", "u"]
    
    while cont<len(frase):
        
        if nova_frase[cont] in vogais:
            
             nova_frase[cont] = str.upper(frase[cont])
             
                
        con+=1
        
    return nova_frase