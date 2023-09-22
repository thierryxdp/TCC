def acima_da_media(notas):
    "Retorne as notas acima da media das notas dadas;lista->lista"
    
    media=sum(notas)/len(notas)
    notas.append(media)
    list.sort(notas)
    x=notas.index(media)
    from math import ceil
    y=ceil(x)
    
    if int(media)==int(notas[0]):
        return []
    else:
    	return notas,media,y