def uppCons(texto):
  """Função que recebe como entrada uma frase e retorna a frase com todas as consoantes em maiúsculas"""
 	l = 0
    frase=''
    while i<len(texto):
        if texto[I]  not in 'abcdefjhijklmnopqrstuvwxyzç':
            frase+=texto[l]
  
        if texto[l] in 'abcdefjhijklmnopqrstuvwxyzç':
        	frase+=str.upper(texto[l])
    
    	l+=1
    return frase