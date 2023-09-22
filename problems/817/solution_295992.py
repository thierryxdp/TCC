#Exercício_07:
''' Essa função recebe uma lista contendo todas as notas de uma turma e devolve outra lista contendo as somente
    as notas acima da média. '''
''' list ---> list. '''

def acima_da_media(original_list):
    
    #Definindo o número de termos:
    nt = len(original_list)
    if nt == 1:
        nt = 0
    
    #Definindo a média:
    media = sum(original_list)/len(original_list)
    
    #Introduzindo a média na lista:
    list.extend(original_list, [media])
    
    #Ordenando a lista:
    list.sort(original_list)
    
    #Deletando os números menores:
    del(original_list[0:(int(list.index(original_list, media)))+1])
    
    #Deletando o possível acrécimo:
    if original_list[0] == 5:
        del(original_list[0])
    
    #Retornando a lista:
    return original_list