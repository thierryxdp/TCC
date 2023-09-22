def melhor_volta(tempos):
    """Funcao que dada uma matriz com os tempos em segundos dos corredores
    em cada volta retorna uma tupla informando de quem foi a melhor volta
    o tempo dessa volta e o numero dela
    list -- tuple"""
    mlhrs_voltas = []
    volta = []
    for i in range(len(tempos)):
        corredor = tempos[i]
        mlhr_volta = min(matriz[i])
        x = list.index(tempos[i], mlhr_volta)
        volta = volta + [x]
        mlhrs_voltas = mlhrs_voltas + [mlhr_volta]
        temp_camp = min(mlhrs_voltas)
    campeao = list.index(mlhrs_voltas, volta_camp) 
    volta_camp = volta[campeao]
    return (campeao+1, temp_camp, volta_camp+1)