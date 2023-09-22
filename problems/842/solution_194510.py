def pontos_por_time(lista):
    """Função que retorna o numero total de pontos de dois times dados seus jogos
    de ida e de volta
    entrada: lista, lista
    saida: dicionario"""
    gols_part1 = lista[2:3]
    gols_part2 = lista[5:] 
    nome_t1 = lista[0:1]
    nome_t2 = lista[3:4]
    if gols_part1[0:1] > gols_part1[1:] and gols_part2[1:] > gols_part2[0:1]:
        return {str(nome_t1)[2:-2]:6 , str(nome_t2)[2:-2]:0}
    elif gols_part1[0:1] > gols_part1[1:] and gols_part2[1:] == gols_part2[0:1]:
        return {str(nome_t1)[2:-2]:4, str(nome_t2)[2:-2]:1}
    if gols_part1[0:1] < gols_part1[1:] and gols_part2[1:] < gols_part2[0:1]:
        return {str(nome_t1)[2:-2]:0, str(nome_t2)[2:-2]:6}
    elif gols_part1[0:1] < gols_part1[1:] and gols_part2[1:] == gols_part2[0:1]:
        return {str(nome_t1)[2:-2]:1,str(nome_t2)[2:-2]:4}
    else:
        return {str(nome_t1)[2:-2]:2, str(nome_t2)[2:-2]:2}