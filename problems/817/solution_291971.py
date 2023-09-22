def acima_da_media(notas):
    media = sum(notas)//len(notas)
    insere = list.append(notas,media)
    ordena_int = list.sort(notas)
    posicao = list.index(notas,media)
    
    
    return notas[posicao+1:]