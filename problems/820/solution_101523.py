def posLetra(frase,letra,n):
    """ Funcao que dada uma string, letra e numero retorna a posição da string aquela 
    ocorrência da letra está. Se houver menos ocorrência , a função retorna -1
    str, str, int--> -1"""
    i=0
    listaletras=[]
	
    while i < len(frase):
        if frase[i] in letra:
            listaletras+=[i]
        i+=1
        
    if len(listaletras)< n:
    	return -1
    else:
    	return listaletras[n-1]