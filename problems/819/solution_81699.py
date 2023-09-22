def filtraMultiplos(multiplos,n):
    "Filtra os 'múltiplos' de um número 'n'; list, int -> list"
    x = 0
    lista=[]
    tamanho = len(multiplos)
    while(x < tamanho):
        y = multiplos[x]%n
        if y == 0:
            lista.append(multiplos[x])
        x = x+1
    return lista