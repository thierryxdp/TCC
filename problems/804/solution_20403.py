def filtra_pares (n1, n2, n3, n4):
    tupla_original = n1, n2, n3, n4
    if tupla_original[0] % 2 == 0:
        tupla_par = tupla_original[0]
        if tupla_original[1] % 2 == 0:
      		tupla_par = tupla_original[0] + tupla_original[1]