def pontos_por_time(lista):
    """list -> list;
    Função que recebe uma lista de dois elementos, onde cada
    elemento é também uma lista que contém o número de gols
    em dois jogos de futebol entre dois times, e retorna um 
    dicionário com o nome dos times e suas pontuações."""
    lista = ['Cormengo', 'Flamínthians', [gc1(x),gf1(x)]],
    ['Flamínthians','Cormengo',[gc2(x),gf2(x)]]
    def gc1(x):
        return int(x)
    def gf1(x):
        return int(x)
    def gc2(x):
        return int(x)
    def gf2(x):
        return int(x)
    time = {'Cormengo':pontosC, 'Flamínthians':pontosF}
    #jogo 1
    pontosC1 = pontosF1 = 0
    if gc1 > gf1:
        pontosC1 = pontosC + 3
    if gc1 < gf1:
        pontosF1 = pontosF + 3
    if gc1 == gf1:
        pontosF1 = pontosF1 + 1
        pontosC1 = pontosC1 + 1
    #jogo 2
    pontosC2 = pontosF2 = 0
    if gc2 > gf2:
        pontosC2 = pontosC2 + 3
    if gc2 < gf2:
        pontosF1 = pontosF2 + 3
    if gc2 == gf2:
        pontosF2 = pontosF2 + 1
        pontosC2 = pontosC2+ 1
    pontosC = pontosC1 + pontosC2
    pontosF = pontosF1 + PontosF2
    return time