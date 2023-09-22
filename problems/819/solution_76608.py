def filtraMultiplos(lista, x) :
    multi = []
    for i in len(lista) - 1 :
      if lista[i]//x == 0 :
        multi.append(lista[i])

    return multi