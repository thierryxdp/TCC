def acima_da_media (notas):
    '''calcula e retorna a lista de notas que ficaram acima da média;
    list->list'''
    
    media=sum(notas)/len(notas)
    list.append(media)
    list.sort(notas)
    i=list.index(notas,media)
    
    return notas[i+1:]