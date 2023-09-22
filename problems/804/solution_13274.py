def filtra_pares( tupla ):
        for i in range(4):
        tupla = tupla + (tupla%2 == 0)
        return tupla