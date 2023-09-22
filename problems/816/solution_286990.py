def maiores(lista,n):
    nova_lista=lista+[n]
    list.sort(nova_lista)
    i=int(list.index(nova_list))+1
    lista_maiores=nova_lista[i: ]