def repitidos(lista): 
    '''funçao que retorna o número de vezes que um elemento é igual ao anterior na lista de entrada'''
    '''list->int'''
    i=1
    resposta=0
    while i < len(list):
        if lista[i]==lista[i-1]: 
            resposta=resposta+1 
        i=i+1 
    return resposta