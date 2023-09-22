def melhor_volta(matriz):
    '''função que verifica, calcula e retorna de quem foi a melhor volta em uma corrida, informando também o tempo e a devida volta. como entrada, recebe uma matriz 6x10 com os tempos dos jogadores; list(lists) -> tuple'''
    
    menores = []
    for i in range(len(matriz)):
        menores.append(min(matriz[i]))
        menor = min(menores)
        
        if menor in matriz[i]:
            quem = matriz[i]+1
            qual = matriz[i].index(min(menores))+1
            
    return (quem, menor, qual)