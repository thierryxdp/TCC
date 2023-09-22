def melhor_volta(mat):
    """Função que recebe um matriz 6x10 com os tempos em
    segundo dos corredores em cada volta e retorna uma tupla 
    informando de quem foi a melhor volta, com qual tempo e em 
    que volta.
    mat->tupla
    """
    melhor_kart = -1
    melhor_tempo = -1
    melhor_volta = -1
    lista = []
    for v in mat:
        list.append(lista, min(v))
    melhor_tempo = min(lista)
    i = 0
    for v in mat:
        i = i + 1
        if melhor_tempo in v:
            melhor_kart = i
            melhor_volta = list.index(v, melhor_tempo) + 1
    return melhor_kart, melhor_tempo, melhor_volta