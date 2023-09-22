def carros(Pessoas,Capacidade_carros=5):
    return ((Pessoas)%(Capacidade_carros))
    if ((Pessoas)%(Capacidade_carros))>0:
        return((Pessoas)//(Capacidade_carros))+1
    else:
        return((Pessoas)//(Capacidade_carros))