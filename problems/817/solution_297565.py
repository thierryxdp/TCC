def maiores_que(lista_numero,n):
    '''Ao receber uma lista numérica ordenada, recebe também um número n e
insere n na lista na ordem correta e retorna uma nova lista com o pedaço
da lista com os elementos maiores que n. list, int --> list'''
    lista = lista_numero[:]
    list.append(lista,n)
    list.sort(lista)
    return lista[int(list.index(lista,n))+1:]

def acima_da_media(lista_nota):
    '''Recebe uma lista com notas de alunos, calcula a media das
notas e retorna as notas que estão acima da media.
list --> list'''
    media = sum(lista_nota)//len(lista_nota)
    return maiores_que(lista_nota,media)