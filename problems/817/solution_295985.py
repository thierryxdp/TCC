#Exercício_07:
''' Essa função recebe uma lista contendo todas as notas de uma turma e devolve outra lista contendo as somente
    as notas acima da média. '''
''' list ---> list. '''

def acima_da_media(list_x, media):
    
    #Introduzindo a média na lista:
    list.extend(original_list, [media])
    
    #Ordenando a lista:
    list.sort(original_list)
    
    #Deletando os números menores:
    del(original_list[0:(int(list.index(original_list, media)))+1])
    
    #Retornando a lista:
    return original_list