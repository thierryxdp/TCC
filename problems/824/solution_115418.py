def uppCons(texto):
    """Função que recebe como entrada uma frase e retorna a frase com todas as consoantes em maiúsculas"""
    l = 0
    frase=''
    while l<len(texto):
        
        if texto[l]  not in 'bcdfgjhjklmnpqrstvwxyzç':
            
            frase+=texto[l]
  
        if texto[l] in 'bcdfgjhjklmnpqrstvwxyzç':
            
            frase+=str.upper(texto[l])
    
    	l+=1
    return frase