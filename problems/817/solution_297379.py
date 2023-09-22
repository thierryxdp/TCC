def maiores(lista,n):
    ''' funcao recebe uma lista e um int, e retorna os elementos maiores que n, list,int-->list'''
    list.insert(lista,0,n)
    list.sort(lista)
    return lista[list.index(lista,n)+1:]



def acima_da_media(lista):
    '''funcao recebe uma lista com a notas dos alunos e retorna uma lista com as notas acima da media,list-->int'''
    if(len(list)==1):
        return: []
        else:
    n= sum(lista)/len(lista)
         return maiores(lista,n)