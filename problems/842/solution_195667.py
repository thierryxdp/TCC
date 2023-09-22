def pontos_por_time(ida, volta):
    "Retorne a pontuação das equipes através dos resultados dos jogos de ida e volta: lista-> dicionário"
    if ida[1]>ida[2]:
        pc=3
        pf=0
    elif ida[1]<ida[2]:
        pc=0
        pf=3
    else:
        pc=1
        pf=1
    if volta[1]>volta[2]:
        pc=pc+3
        pf=pf+0
    elif volta[1]<volta[2]:
        pc=pc+0
        pf=pf+3
    else:
        pc=pc+1
        pf=pf+1
        
        return {ida[0]:pc, ida[1]:pf}