def melhor_volta(matriz):
    'dado uma matriz onde os indices 1-6 são os corredores e os indices 1-10 são o tempo de cada volta, retorna de quem foi a melhor volta'
    comparador=[]
    for corredores in matriz:
        for tempo in corredores:
            list.append(comparador,tempo)
    posicao_menor_tempo=list.index(comparador,min(comparador))
    if posicao_menor_tempo<=9:
        return tuple((1,min(comparador),posicao_menor_tempo+1))
    if 9<posicao_menor_tempo<=19:
        return tuple((2,min(comparador),posicao_menor_tempo+1))
    if 19<posicao_menor_tempo<=29:
        return tuple((3,min(comparador),posicao_menor_tempo+1))
    if 29<posicao_menor_tempo<=39:
        return tuple((4,min(comparador),posicao_menor_tempo+1))
    if 39<posicao_menor_tempo<=49:
        return tuple((5,min(comparador),posicao_menor_tempo+1))
    if 49<posicao_menor_tempo<=59:
        return tuple((6,min(comparador),posicao_menor_tempo+1))