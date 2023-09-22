def acima_da_media(lista):
    '''Esta função recebe como parametro uma lista com as notas dos alunos de uma turma e retorna as notas acima da média.
list->list'''
    
    media=sum(lista)//len(lista)
    lista.insert(0,media)
    list.sort(lista)
    a=list.index(lista,media)
    lista_nova=lista[a+1:]
    return lista_nova