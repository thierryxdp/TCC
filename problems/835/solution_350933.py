def melhor_volta(matriz):
    """Recebe uma matriz 6 x 10 com os temps em segundo dos
    corredores em cada volta, retornando uma tupla informando
    de quem foi a melhor volta, com qual tempo e em que volta;
    list -> tuple"""
    corredor = 0
    melhor_volta_pilotos = ()
    for linha in matriz:
        corredor += 1
        melhor_volta_pilotos += ((corredor, min(linha), linha.index(min(linha)) + 1), )

    tempos = ()
    for tabela in melhor_volta_pilotos:
        tempos += (tabela[1],)

    for tabela in melhor_volta_pilotos:
        if min(tempos) == tabela[1]:
            return tabela