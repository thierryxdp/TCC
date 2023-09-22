def melhor_volta(matriz):
    '''A partir da matriz 6x10 de entrada com os tempos das
    10 voltas de cada corredor retorna qual corredor
    concluiu uma volta no menor tempo,que tempo foi esse
    e em que volta isso foi feito
    list -> tuple'''
    tempos = []
    for corredor in matriz:
        for tempo in corredor:
            list.append(tempos,tempo)
    menor_t = min(tempos)
    corredor = ((list.index(tempos,menor_t))//10)+1
    volta = ((list.index(tempos,menor_t))%10)+1
    return (corredor,menor_t,volta)