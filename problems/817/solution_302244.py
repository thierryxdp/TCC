def maiores(lista,n):
    '''Função que dada uma lista e um numero n retorne uma lista com os numeros maiores que n;list,int->list'''
    list.append(lista,n)
    list.sort(lista)
    i=list.index(lista,n)
    return lista[i+1:]
def acima_da_media(lista):
    ''' retornará as notas dos alunos que ficaram acima da média;list->list'''
    media=sum(lista)/len(lista)
    return maiores(lista,media)