def acima_da_media(lista):
    '''retorna todas as notas da turma que
    ficaram acima da media; list->list'''
    media=(sum(lista)/len(lista))
    list.append(lista,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    list.remove(lista,media)
    
    return lista[posicao:]