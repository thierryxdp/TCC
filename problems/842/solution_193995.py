def pontos_por_time(lista1,lista2):
    """Função que retorna o numero total de pontos de dois times dados seus jogos
    de ida e de volta
    entrada: lista, lista
    saida: dicionario"""
    nome_time1 = lista1[0:1]
    nome_time2 = lista2[0:1]
    gols_part1 = lista1[2:]
    gols_part2 = lista2[2:]
    if (gols_part1[0:1] > gols_part1[1:]) and (gols_part2[1:] > gols_part2[0:1]):
        return {nome_time1:6 , nome_time2:0}
    elif (gols_part1[0:1] > gols_part1[1:]) and (gols_part2[1:] = gols_part2[0:1]):
        return {nome_time1:4, nome_time2:1}
    if (gols_part1[0:1] < gols_part1[1:]) and (gols_part2[1:] < gols_part2[0:1]):
        return {nome_time1:0, nome_time2:6}
    elif (gols_part1[0:1] < gols_part1[1:]) and (gols_part2[1:] = gols_part2[0:1]):
        return {nome_time1:1, nome_time2:4}
    else:
        return {nome_time1:2, nome_time2:2}