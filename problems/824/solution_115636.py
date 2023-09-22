def uppCons(frase):
    """Função que dada uma frase no formato de string, retorna essa mesma frase com todas suas consoantes em maiúsculas,
    enquanto os demais caracteres continuam como na frase original;
    str-->str"""
    i=0
    frase2=''
    while i<len(frase):
        if frase[i] not in 'bcçdfghjklmnpqrstvwxz':
            frase2+=frase[i]
  
        if frase[i] in 'bcçdfghjklmnpqrstvwxz':
        	frase2+=str.upper(frase[i])
    
    	i+=1
    return frase2