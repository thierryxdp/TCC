def faltante(lista):
    '''Funçao que retorna o numero inteiro que falta
    em uma lista numerada de 1 a N.'''
    
    
    total=[1]
    x=2
    
   	while len(total)<len(lista)+1:
    	total=total+[x]
    	x=x+1
    
    t=list.sort(total)
    l=list.sort(lista)
    
    y=0
    
    while y<len(t)
    	if t[y]!=l[y]
    	y=y+1
    return t[y]