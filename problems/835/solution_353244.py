def melhor_volta(pilotos_e_voltas):
    """dada uma lista pilotos_e_voltas 6x10, na qual as linhas são os pilotos
    e as colunas seus respectivos tempos de volta, retorna uma tupla 
    o nome de quem obteve o melhor tempo de volta e o tempo em segundos,
    e em que volta
    list --> tuple"""
    melhor_volta=pilotos_e_voltas[0][0]
    for piloto in pilotos_e_voltas:
        for volta in piloto:
            if volta < melhor_volta:
                melhor_volta=volta
                melhor_piloto=list.index(pilotos_e_voltas,piloto)+1
    return (melhor_piloto,melhor_volta)