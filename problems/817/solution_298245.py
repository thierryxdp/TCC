def acima_da_media(notas):

    media = (sum(notas)/len(notas))
    list.append(notas,media)
    list.sort(notas)
    notas[list.index(notas,media):]
    acima = notas[list.index(notas,media):]
    list.remove(acima,media)
    
     	return acima