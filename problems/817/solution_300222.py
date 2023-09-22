def acima_da_media(notas):
    
    media=sum(notas)/len(notas)
    
    list.sort(notas)
    x= list.index(notas,media)
    del notas[:x+1]
    return notas