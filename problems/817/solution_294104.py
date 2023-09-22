def acima_da_media(notas):
    
    media=sum(notas)/len(notas)
    list.sort(notas)
    primeira_aprovado=list.index(notas,media)
    
    return notas[primeira_aprovado:]