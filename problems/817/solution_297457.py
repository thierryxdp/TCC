def maiores(lista,n):
    '''
    	Função que dada uma lista de inteiros e um numero inteiro 'n', retorna outra lista maiores que 'n', em ordem crescente
        list ->list
    '''
    list.append(lista,n)
    list.sort(lista)
    return lista[list.index(lista,n)+1:]

def acima_da_media(lista):
    '''
    	Função que recebe uma lista com notas de alunos e retorna uma lista ordenada com as notas acima da media
        list->list
    '''
    media = sum(lista)//len(lista)
    return maiores(lista,media)