def melhor_volta(m):
    contador = 0
    acumulador = 0
    min = 999999
    i = 0
    j = 0
    if len(m) != 0:
        while i < len(m):
            j = 0
            while j < len(m[i]):
                if m[i][j] < min:
                    min = m[i][j]
                    mc = i
                    mv = j
                j += 1
            i += 1
        return (mc, min, mv)