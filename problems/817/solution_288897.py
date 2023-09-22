def acima_da_media(lista):
    """dada uma lista com as notas dos alunos
de uma turma, retorna uma lista ordenada com
as notas que ficaram acima da média"""
    media = sum(lista)/len(lista) #acha a média
    lista = lista + [media] #concatenar para impor a media entre os numeros
    list.sort(lista)
    posicao = list.index(lista,media) #acha a posição
    return lista[2+posicao:] #tira a posição anterior e 'exclui' a media para não aparecer