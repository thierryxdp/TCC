def faltante(lista):
    '''Dada uma lista com N-1 inteiros numerados de 1 a N,
    descobre qual numero inteiro deste intervalo esta faltando
    list -> int'''
    
    list.sort(lista)
    i=0
    
    if 1 not in lista:
        return 1
    
    while i<len(lista)-1:
        
        if lista[i+1]-lista[i]!=1:
            return lista[i]+1
       
        i=i+1
        return lista[i]+1