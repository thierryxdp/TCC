def maiores (lista,n):
    '''Função que dada uma lista com as notas dos alunos de uma turma,
    retorna uma lista ordenada com as notas que ficaram acima da média.
    lista,int->str'''
    if n not in lista:
        list.append(lista,n)
        
    list.sort(lista)
    ind = list.index(lista,n)
    listaf = lista[ind+1:]
    
    return listaf

def acima_da_media(lista):
    '''...'''
    
    media=sum(lista)/len(lista)
    
    return maiores(lista,media)