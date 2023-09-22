#Exercício_07:
''' Essa função recebe uma lista contendo todas as notas de uma turma e devolve outra lista contendo as somente
    as notas acima da média. '''
''' list ---> list. '''

def acima_da_media(original_list):
    
    #Definindo a média:
    media = sum(original_list)/len(original_list)
    
    #Introduzindo a média na lista:
    list.extend(original_list, [media])
    
    #Ordenando a lista:
    list.sort(original_list)
    
    #Deletando os números menores:
    del(original_list[0:(int(list.index(original_list, media)))+1])
    
    #Retornando a lista:
    return original_list