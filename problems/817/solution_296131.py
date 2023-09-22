def acima_da_media(lista):
    
    list.sort(lista)
    list.reverse(lista)
    
    media= sum(lista)/len(lista)
    nota_acima_de= list.index(lista,media)
    
    nova_lista=lista[:nota_acima_de]
    list.reverse(nova_lista)
    return nova_lista