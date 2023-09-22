def maiores(lista,n):
    '''Retorna os valores da lista que são maiores que n
    str,int --> list'''
    lista[0:0] = [n]
    list.sort(lista)
    maiores = lista[(list.index(lista,n))+1:]
    return maiores

def acima_da_media(lista):
    '''Retorna uma lista com as notas acima da media da turma
    lista --> lista'''
    media = int(sum(lista)/len(lista))+1