def lingua_p(frase):
    separada=list(frase)
    if 'a' in separada:
    	z=list.index(separada,'a')
        list.insert(separada,z+1,'p')
    if 'e' in separada:
    	v=list.index(separada,'e')
        list.insert(separada,v+1,'p')
    if 'i' in separada:
    	u=list.index(separada,'i')
        list.insert(separada,u+1,'p')
    if 'o' in separada:
    	p=list.index(separada,'o')
        list.insert(separada,p+1,'p')
    if 'u' in separada:
    	t=list.index(separada,'u')
        list.insert(separada,t+1,'p')
    separada=separada.join(separada)    
    return separada