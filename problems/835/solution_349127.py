def melhor_volta(m):
    contagem = 0
    lista = []
    total = 0
    for i in m:
        lista.append(min(i))
    primeiro = min(lista)
    for j in m:
        if primeiro in j:
            c = m[j].index(primeiro)
            return primeiro,j,c