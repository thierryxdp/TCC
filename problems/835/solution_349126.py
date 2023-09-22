def melhor_volta(placar):
    '''função que recebe uma matriz 6x10 com o placar dos corredores
    de um kart em cada volta, e retorna uma tupla informando de quem foi
    a melhor volta. list-> tuple'''
    n=float('inf')
    lista=[0,n,0]
    for l in range(6):
        for c in range(10):
            if placar[l][c] < lista[1]:
                lista=l+1,placar[l][c],c+1
    return lista