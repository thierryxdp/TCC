l = [['Cormengo', 'Flamínthians', [1,0]], ['Flamínthians', 'Cormengo', [2, 2]]]
def pontos_por_time(jogo):
    resultado = {}
    for ind,[i,k,c] in enumerate(jogo):
        if ind == 0:
            resultado[i] = resultado[k] = 0
        if c[0] > c[1]: resultado[i] += 3
        elif c[0] == c[1]:
            resultado[i] += 1
            resultado[k] += 1
        else: resultado[k] += 3
    return resultado