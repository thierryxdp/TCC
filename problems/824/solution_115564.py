def uppCons(texto):
    """Funçao  que receba uma frase como parametro de entrada e retorna a mesma frase com todas as suas consoantes em 
maiuculas sendo que o restante indiferente continuam no tamanho normal, str->str"""

    l=0
    frase=''
    while l<len(texto):
        if texto[l]  not in 'bcçdfghjklmnpqrstvwxz':
            frase+=texto[l]
  
        if texto[l] in 'bcçdfghjklmnpqrstvwxz':
        	frase+=str.upper(texto[l])
    
    	l+=1
    return frase