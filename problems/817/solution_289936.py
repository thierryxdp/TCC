def acima_da_media(lista):
    """Para listar as notas que ficaram a cima da média, digite;
    int->int"""
    a=sum(lista)
    b=len(lista)
    c=a/b
    
    if c not in lista:
        list.append(lista,c)
    	lista=sorted(lista)
    	x=list.index(lista,c)
    	y=c+1
        return lista[y:]
    else:
        lista=sorted(lista)
    	x=list.index(lista,c)
    	y=c+1