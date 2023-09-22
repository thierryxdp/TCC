def repetidos(lista):
    ''' funcao que recebe uma lista e retorna o numero de vezes que esse elemento e egual ao seu anterior; list-> int'''
    i=0
    a=0
    
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            
            a+=1
        
        i+=1

    return a