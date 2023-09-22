def carros(Pessoas,Capacidade_carros=5):
    if ((Pessoas)%(Capacidade_carros))<(Capacidade_carros):
        ((Pessoas)//(Capacidade_carros))+1
    else:
        ((Pessoas)//(Capacidade_carros))