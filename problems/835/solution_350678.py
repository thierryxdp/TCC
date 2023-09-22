def melhor_volta(matriz):
    '''funcao que ao receber uma matriz 6x10 a qual as linhas sao os competidores de uma corrida e as colunas o tempo deles em cada volta, retorna quem teve a melhor volta, o tempo e em qual volta;
       list(list)-> tuple'''
    menorestempos=[]
    for linha in range(len(matriz)):
        list.append(menorestempos,min(matriz[linha]))
    return (list.index(menorestempos,min(menorestempos))+1,min(menorestempos),list.index(matriz[list.index(menorestempos,min(menorestempos))],min(menorestempos))+1)