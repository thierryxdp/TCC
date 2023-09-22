def repetidos(numeros):
    '''recebe uma lista de números e retorna o número 
    de vezes que um elemento da lista é igual ao elemento 
    anterior; list -> int'''
    
    i = 0
    j = i + 1
    
    while i  < len(numeros):
        if numeros[i] == numeros[j]:
            return 1
      
    i = i+1