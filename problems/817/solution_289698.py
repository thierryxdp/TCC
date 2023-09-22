def acima_da_media(notas):
    notas[:]=notas
    list.sort(notas)
    funcao= sum(notas)/len(notas)
    return funcao