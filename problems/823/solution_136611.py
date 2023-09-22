def faltante(L):
    '''Dada uma lista com N-1 inteiros numerados de 1 a N, retorna o número inteiro que está faltando;list->int'''
    
    
    list.sort(L)
    
    
    for i in range(0,len(L)):
        if L[0] != 1:
            return 1
        if len(L) == L[len(L)-1]:
            return len(L)+1
        if(L[i]-(L[i-1]))!= 1 and (L[i]-(L[i-1]))>0:
            return i+1
   		else:
        	return len(L)+1