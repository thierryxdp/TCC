def repetidos(lista_num):
    ''' Função que retorna quantas vezes 
        um elemento da lista dada é igual 
        ao elemento anterior
        list -> int '''
    
    i = 1
    soma = 0
    
    while i < len(lista_num):
        if lista_num[i-1] == lista_num[i]:
            soma = soma + 1
            
        i = i + 1
        
    return soma