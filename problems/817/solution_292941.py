import math
def acima_da_media(lista):
    '''retorna todas as notas da turma que
    ficaram acima da media; list->list'''
    media=math.ceil((sum(lista)/len(lista)))
    list.append(lista,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    del lista[posicao]
    
    return lista[posicao:]