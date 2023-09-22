def melhor_volta(matriz):
    """dado uma matriz 6 x 10 que represente 6 corredores e 10
    voltas, com o elemento de cada posição representando o tempo
    daquele corredor naquela volta, a função retorna uma tupla 
    com a melhor volta, o corredor que a fez e a vez que ele fez;
    list -> tuple"""
    listaminimos = [] #tempos minimos
    for x in matriz: #x são os tempos de cada corretor
        list.append(listaminimos,min(x))#minimos de cada corredor
        a = min(listaminimos)#menor tempo ao todo
        b = list.index(listaminimos,a)#indice do menor tempo
        for y in matriz[b+1]:
            if y == a:
	            c = list.index(x,y)
    return (b+1, a, c+1)