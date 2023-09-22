def melhor_volta(matriz):
    '''Dado uma matrix 6x10, simulando tempos de corredores em voltas, retorna uma tupla,
    informando, de quem foi a volta mais rápida, com qual tempo, e em qual volta.
    list -> tup'''
    volta_rap=[]
    num_volta=[]
    for i in (matriz):
        indice=list.index(i,min(i))+1
        list.append(volta_rap,min(i))
        list.append(num_volta,indice)
	vol=min(volta_rap)
    return (list.index(volta_rap,vol)+1,vol,num_volta[list.index(volta_rap,vol)])