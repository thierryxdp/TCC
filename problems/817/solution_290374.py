def acima_da_media(lista):
    soma_de_notas = sum(lista)
    tamanho = len(soma_de_notas)
    media = soma_de_notas / tamanho
    listamaiores = []
    for notas in lista:
        if(notas > media):
            list.append(listamaiores, notas)
    list.sort(listamaiores)
    return listamaiores