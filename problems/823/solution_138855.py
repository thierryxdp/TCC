def faltante(lista):
    '''Funçao que retorna o numero inteiro que falta
    em uma lista numerada de 1 a N. list -> int'''
    
    
    total=[]
    x=1
    
    while len(total)<len(lista)+1:
        total=total+[x]
    	x=x+1
    
    t=sorted(total)
    l=sorted(lista)
    
    y=0
    
    while y<len(total):
    	if t[y]!=l[y]:
    		y=y+1
    return t[y]