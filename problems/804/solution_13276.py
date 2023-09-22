def filtra_pares( tupla ):
        for i in range(4):
        tupla = tupla + (tupla[i] %2 == 0)
         return tupla