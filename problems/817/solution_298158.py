def acima_da_media(notas):
    "Retorne as notas acima da media das notas dadas;lista->lista"
    
    media=sum(notas)/len(notas)
    notas.append(media)
    list.sort(notas)
    x=notas.index(media)
  
    if int(media)==int(notas[0]):
        return []
    elif int(media)==notas[int(media)-1]:
        return notas[int(x)+2:]
    
    else:
    	return notas[int(x)+1:]