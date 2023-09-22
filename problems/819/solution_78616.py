def filtraMultiplos(lista,num):
    multi = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]/num == 0: 
            multi =[multi + lista[proximo],]
            proximo = proximo + 1
    return multi