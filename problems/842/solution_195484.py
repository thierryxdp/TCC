def pontos(pontostime1,pontostime2):
    if pontostime1==pontostime2:
        return p1=p2=1
    elif pontostime1>>pontostime2:
        return p1=3
    else return p2=3

def pontos_por_time(nometime):
    return {nometime: pontos(pontostime1,pontostime2)}