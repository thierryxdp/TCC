def acima_da_media():
    
    media=sum(notas)/len(notas)
    list.sort(notas)
    primeira_media=list.index(notas,media)
    
    return notas[primeira_media:]