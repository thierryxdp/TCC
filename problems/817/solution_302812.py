def acima_da_media(lista,):
    ''' funcao que dada uma lista com notas de alunos retorna todos as notas acima da media (5)
    list >>> list'''
    nova_lista=[]
    
    while len(lista) > 0:
        if lista[0] >= 5:
            nova_lista.append(lista[0])
            lista.remove(lista[0])
        if len(lista)==0:
            nova_lista.sort()
            return nova_lista
        if lista[0]< 5:
            lista.remove(lista[0])
    nova_lista.sort()
    return nova_lista