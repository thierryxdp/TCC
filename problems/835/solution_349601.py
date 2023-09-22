def melhor_volta(matriz):
    'dado uma matriz onde os indices 1-6 são os corredores e os indices de 1-10 são os tempos de cada volta, retorna o corredor,menor tempo e a volta'
    lista_de_menores_tempos=[]
    for corredor in matriz:
        list.append(lista_de_menores_tempos,min(corredor))
    corredor=list.index(lista_de_menores_tempos,min(lista_de_menores_tempos))+1
    volta_de_menor_tempo=min(lista_de_menores_tempos)
    numero_da_volta=list.index(matriz[corredor-1],volta_de_menor_tempo)
    return tuple((corredor,volta_de_menor_tempo,numero_da_volta))