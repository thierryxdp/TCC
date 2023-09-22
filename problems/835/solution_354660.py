def melhor_volta(matriz):
    '''Função que calcula o melhor tempo de volta entre os corredores;
    Recebe uma matriz com tempos;
    Retorna a melhor volta.'''
    best_time = []
    competidores = [ '1','2','3','4','5','6']
    for i in matriz:
        a = min(i)
        list.append(best_time,a)
    c = list.index(best_time,min(best_time))
    b = list.index(matriz[c],min(matriz[c]))
    return tupla(competidores[c] + best_time[c] + b)