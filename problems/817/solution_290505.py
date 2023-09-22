def acima_da_media(lista):
    #Dada uma lista com notas de um aluno retorna ordenadamente em uma nova lista as notas que ficaram acima da média. list->list
    list.sort(lista)
    media = sum(lista)/len(lista)
    nova_lista = list()
    for i in lista:
        if i > media:
            list.extend(nova_lista,[i])
    return(nova_lista)