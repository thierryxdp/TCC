def uppCons(frase):
    '''retorna a frase dada com todas as suas consoantes maiúsculas'''
    '''str -> str''' 
    
    i=0
    
    
    while i < len(frase):
        if frase[i] in 'aeiouAEIOU':
            a=str.upper(frase,i)
            
            return a