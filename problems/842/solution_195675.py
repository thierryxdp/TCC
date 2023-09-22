def pontos_por_time(lista):
    times = lista[0]
    gol = lista[1]
    cor = gol[0]
    fla = gol[1]
    somafla = 0
    somacor = 0
    if cor > fla:
        somacor = somacor+3
    if fla > cor:
        somafla = somafla+3
    if fla == cor:
        somafla = somafla+1
        somacor = somacor+1
        return [somafla,somacor]