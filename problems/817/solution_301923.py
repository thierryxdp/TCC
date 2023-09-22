def acima_da_media(x):
    qntdd_alunos=int(len(x))
    media=sum(x)/qntdd_alunos
    nova_lista=x+[media]
    nova_lista1=list.sort(nova_lista)
    i=int(list.index(nova_lista,media))+1
    lista_maiores=[]+nova_lista[i: ]
    return lista_maiores