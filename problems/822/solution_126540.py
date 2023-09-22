def repetidos(lista):
    '''Funçao que recebe uma lista, e retorna o número de 
       vezes que um elemento da lista é igual ao elemento
       anterior. 
       : param lista: list
       : return: int
    '''
    i=0
    quantas_vezes=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            quantas_vezes=quantas_vezes+1
        i=i+1
    return quantas_vezes