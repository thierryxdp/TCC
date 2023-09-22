#Exercício_06:
''' Essa função recebe uma lista e um número inteiro, ela retorna uma outra lista ordenada de maneira crescente
    que contem somente os números que forem maiores do que o int recebido. '''
''' list, int ---> list. '''

def maiores(original_list, number):
    
    #Introduzindo o número na lista:
    list.extend(original_list, [number])
    
    #Ordenando a lista:
    list.sort(original_list)
    
    #Deletando os números menores:
    del(original_list[0:(int(list.index(original_list, number)))+1])
    
    #Retornando a lista:
    return original_list