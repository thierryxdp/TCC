import statistics
def media8(lista):
    "retorna a média da lista de oito em oito valores"
    i = 0
    medias = []
    for i in range(len(lista)):
        j = 0
        diario = []
        while j < 8:
            diario.append(lista[i])
            i += 1
            j += 1
        media = statistics.mean(diario)
        medias.append(media)
    return medias