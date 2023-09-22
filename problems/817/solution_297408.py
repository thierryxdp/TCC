def acima_da_media(lista):
    """retorna as notas acima da média"""
    media = sum(lista) // len(lista)   #divide a soma dos elementos pela quantidade
    list.append(lista,media)           #adiciona a média na lista
    list.sort(lista)                   #ordena a lista
    posicao = list.index(lista,media)  #retorna o índice da média
    del lista [:posicao+1]             #remove a média e os elementos anteriores
    if media in lista:                 #remove a média caso ela esteja na lista
        list.remove(lista, media)
    return lista