def pontos_por_time (lista):
    casa = lista[0]
    fora = lista[1]
    gol_casa_jogo1 = lista [2]
    gol_fora_jogo1 = lista [3]
    If gol_casa_jogo1 > gol_fora_jogo1:
        casa = {casa: 3}
        fora = {fora: 0}
    If gol_fora_jogo1 > gol_casa_jogo1:
        casa = {casa: 0}
        fora = {fora: 3}
    If gol_fora_jogo1 == gol_casa_jogo1:
        casa = {casa: 1}
        fora = {fora: 1}
    gol_casa_jogo2 = [-1]
    gol_fora_jogo2 = [-2]
    If gol_casa_jogo2 > gol_fora_jogo2:
        casa2 = {casa: 3}
        fora2 = {fora: 0}
    If gol_fora_jogo1 > gol_casa_jogo1:
        casa2 = {casa: 0}
        fora2 = {fora: 3}
    If gol_fora_jogo1 == gol_casa_jogo1:
        casa2 = {casa: 1}
        fora2 = {fora: 1}
    return {casa + casa2, fora + fora2}