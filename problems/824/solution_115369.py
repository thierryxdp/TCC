def uppCons(texto):
    """Função que recebe como entrada uma frase e retorna a frase com todas as consoantes em maiúsculas"""
    l=0
    frase=''
    while I<len(texto):
        if texto[I]  not in 'abcdefjhijklmnopqrstuvwxyzç':
            frase+=texto[l]
  
        if texto[I] in 'bcçdfghjklmnpqrstvwxz':
        	frase+=str.upper(texto[I])
    
    	I+=1
    return frase