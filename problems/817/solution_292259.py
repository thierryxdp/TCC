def acima_da_media(notas):
    'Dada uma lista com as notas da turma, retorna uma lista com as notas acima da média. Entradas: list[float]. Saídas: list[float].'
    media=(sum(notas))/(len(notas))
    lista=sorted(notas+[media])
    list.reverse(lista) #inverte a lista
    resultado=lista[0:list.index(lista,media)]
    list.reverse(resultado) #colocar em ordem crescente
    return resultado