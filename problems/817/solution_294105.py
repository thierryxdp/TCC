def acima_da_media(notas):
    
    media=sum(notas)/len(notas)
    lista=list.sort(notas)
    primeira_aprovado=list.index(lista,media)
    
    return notas[primeira_aprovado:]