def pontos_por_time(l):
    classificacao = {l[0][0]:0, l[0][1]:0}
    if l[0][2][0] > l[0][2][1]:
        classificacao[l[0][0]] = classificacao[l[0][0]] + 3
    elif l[0][2][0] == l[0][2][1]:
        classificacao[l[0][0]] = classificacao[l[0][0]] + 1
        classificacao[l[0][1]] = classificacao[l[0][1]] + 1
    else:
        classificacao[l[0][1]] = classificacao[l[0][1]] + 3
    if l[1][2][0] > l[1][2][1]:
        classificacao[l[0][1]] = classificacao[l[0][1]] + 3
    elif l[1][2][0] == l[1][2][1]:
        classificacao[l[0][0]] = classificacao[l[0][0]] + 1
        classificacao[l[0][1]] = classificacao[l[0][1]] + 1
    else:
        classificacao[l[0][0]] = classificacao[l[0][0]] + 3

    return classificacao