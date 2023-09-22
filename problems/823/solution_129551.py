def faltante(lista):
    '''dada uma lista com N-1 inteiros numerados de 1 a N, retorna qual
    número está faltando
    list ->int'''
    list.sort(lista)
    i =0
    num =0
    
    if lista[len(lista)-1] !=len(lista)+1:
        return len(lista)+1
    
    if lista[0] !=1
    	return 1
    
    if lista[1] !=2:
        return 2
    
    while i <len(lista) and int(lista[i+1]) ==int(lista[i])+1:
        num =int(lista[i+1])+1
        i =i+1
  
    return num