def maiores(lista_numeros, n):
    ''' Dada uma lista de numeros inteiros e um numero
    inteiro n, retorna outra lista contendo todos os numeros
    maiores que n da lista anterior
    list, int->list'''
    
    l=lista_numeros
    
        
    list.append(l,n)
    list.sort(l)
    posicao=list.index(l,n)
    l_final=l[posicao+list.count(n):]
    
    return l_final

def acima_da_media(lista):
    '''Dada uma lista com as notas dos alunos de uma turma,
    retorna a lista ordenada com as notas que ficaram 
    acima da media
    list->list'''
    
    media=sum(lista)/len(lista)
   
    
    return maiores(lista, media)