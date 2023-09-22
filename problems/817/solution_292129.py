def maiores(lista, n):
    lista.append(n)
    lista.sort()
    posicao_n = lista.index(n)
    maiores_n = lista[posicao_n + 1:]

    return maiores_n

def acima_da_media(notas_turma):
    media_turma = sum(notas_turma) / len(notas_turma)

    return maiores(notas_turma, media_turma)