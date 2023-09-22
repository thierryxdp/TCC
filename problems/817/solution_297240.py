import math 
def acima_da_media(notas): 
    """ funcao que dada uma lista com as notas dos alunos
        retorna uma lista ordenada com as notas que 
        ficaram acima da média
        : list -> list
    """
    media = int(math.floor(sum(notas)/len(notas))) 
    if media in notas: 
        list.append(notas, media) 
        list.sort(notas) 
        ocorrencia = list.index(notas, media) 
        return notas[ocorrencia+2:] 
    else: 
        list.append(notas, media) 
        list.sort(notas) 
        ocorrencia = list.index(notas, media) 
        return notas[ocorrencia+1:]