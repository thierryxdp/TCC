def filtramultiplos(lista,n):
    i = 0
    multiplos = []
    while i < len(lista):
        lista[i]%n=0
        multiplos = multiplos + lista[i]
    i=i+1
    return multiplos