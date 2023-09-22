def repetidos(lista):
    '''Função que recebe uma lista de números e retorna o 
    número de vezes que o elemento da lista é igual ao 
    elemento anterior.
    
    lista -> int'''
    
    i=0
    num_de_vezes = 0
    
    while i<len(lista):
        if lista[i]==lista[i-1]:
            num_de_vezes.append(1)
        i=i+1
    return num_de_vezes