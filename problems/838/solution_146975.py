a = [23.939,
23.8042,
23.7296,
23.6698,
23.6252,
23.6716,
23.775,
23.8404]

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