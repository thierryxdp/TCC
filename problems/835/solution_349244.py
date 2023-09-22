def melhor_volta(m):
    contagem = 1
    lista = []
    total = 0
    for i in m:
        lista.append(min(i))
    primeiro = min(lista)
    for j in m:
        if primeiro in j:
            return contagem,primeiro,j.index(primeiro)
        else:
            contagem = contagem + 1