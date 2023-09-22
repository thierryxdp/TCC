def melhor_volta(m):
    '''Fucao recebe uma matriz contendo os valores de dez voltas dos seis participantes da corrida e retorna uma tupla contendo o vencendor(o que fizer em menor tempo em segundos), a melhor volta do mesmo e o tempo da melhor volta
list -> tuple'''
    minimo = []
    competidor = 0
    contador = 0
    volta = 0
    for i in m:
        list.append(minimo, min(i))
    valor = min(minimo)
    for i in m:
        contador += 1
        if (valor in i):
            volta = list.index(i, valor)
            competidor = contador
                
    return  (competidor, volta, valor)