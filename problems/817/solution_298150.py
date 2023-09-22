def acima_da_media(notas):
    "Retorne as notas acima da media das notas dadas;lista->lista"
    from math import ceil
    media=sum(notas)/len(notas)
    notas.append(ceil(media))
    list.sort(notas)
    x=notas.index(media)
  
    if int(media)==int(notas[0]):
        return []
    
    else:
    	return notas[int(x)+1:]