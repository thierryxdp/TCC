def conta_numero(numero,matriz):
    '''Esta função retorna a quantidade de ocorrências do número 
    inteiro inserido, na matriz dada.
    int, list -> int'''
    
    ocorrencia=0
            
    for indice in range(len(matriz)):
        ocorrencia=ocorrencia+list.count(matriz[indice], numero)
        
    return ocorrencia