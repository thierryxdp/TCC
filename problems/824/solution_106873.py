def uppCons(frase:str)->str:
    
    """ Função que recebe como entrada uma frase qualquer e retorna a mesma frase 
   		com todas as consoantes maiúsculas.
        
    """
    
    cont = 0
    nova_frase = frase 
    vogais = ["a", "e", "i", "o", "u","ã","á","à","â","é","ê","ô","ó","í"]
    
    while cont<len(frase):
        
        if nova_frase[cont] not in vogais:

            vm = str.upper(nova_frase[cont])
            nova_frase = str.replace(nova_frase,nova_frase[cont],vm)
             
                
        cont+=1
        
    return nova_frase