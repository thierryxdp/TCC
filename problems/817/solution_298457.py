import math
def acima_da_media(notas):
    '''
       Função que recebe uma lista com as notas dos alunos,calcula sua media 
       e retorna uma outra lista as notas que estiveram acima da média aferida
       list --> list
    '''
    
    media = int(math.floor(sum(notas)/len(notas)))
    
    if media in notas:
       notas + [media]
       notas.sort()
       
       outra_lista = list.index(notas,media)
       
       return notas[outra_lista+2:]
    
    else:
       notas + [media]
       notas.sort()
                           
       outra_lista = list.index(notas,media)
       
       return notas[outra_lista+1:]