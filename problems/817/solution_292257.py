def acima_da_media(notas):
    'Dada uma lista com as notas da turma, retorna uma lista com as notas acima da média. Entradas: list[float]. Saídas: list[float].'
    media=(sum(notas))/(len(notas))
    lista=sorted(notas+[media])
    invertida=list.reverse(lista)
    seq=invertida[0:(list.index(invertida,media))]
    resultado=list.reverse(seq)
    return resultado