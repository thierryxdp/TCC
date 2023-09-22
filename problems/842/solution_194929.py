def pontos_por_time(L):
    """A função acima retorna os pontos totais de cada time.
       lista -> dicionário
       Explicação: A função recebe como parâmetro uma lista com duas listas. 
       Seus elementos são os times e seus respectivos pontos nos jogos de 
       ida (primeira lista) e volta (segunda lista).
       Ao interpretar esses dados, a função retorna um dicionário contendo os
       pontos totais de cada time na fase, mais o nome dos times como chave."""
    T1 = L[0][0]
    T2 = L[0][1]
    T1_1 = L[1][1]
    T2_1 = L[1][0]
    pT1 = L[0][2][0]
    pT2 = L[0][2][1]
    pT2_1 = L[1][2][0]
    pT1_1 = L[1][2][1]
    A = 0
    B = 0
    if pT1 > pT2:
        A = A + 3
    if pT1 < pT2:
        B = B + 3
    if pT1 == pT2:
        A = A + 1
        B = B + 1
    if pT1_1 > pT2_1:
        A = A + 3
    if pT1_1 < pT2_1:
        B = B + 3
    if pT1_1 == pT2_1:
        A = A + 1 
        B = B + 1
    return {T1: A, T2: B}

#Teste 1:
#pontos_por_time([['Cormengo', 'Flamínthians', [1, 0]], ['Flamínthians', 'Cormengo', [2, 2]]])--> {'Cormengo': 4, 'Flamínthians': 1}

#Teste 2:
#pontos_por_time([['Tubarões', 'Mercenários', [2, 2]], ['Mercenários', 'Tubarões', [2, 2]]])--> {'Tubarões': 2, 'Mercenários': 2}