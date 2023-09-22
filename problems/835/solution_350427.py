def melhor_volta(matriz):
    '''funcao que ao receber uma matriz 6x10 a qual as linhas sao os competidores de uma corrida e as colunas o tempo deles em cada volta, retorna quem teve a melhor volta, o tempo e em qual volta;
       list(list)-> tuple'''
    menorestempos= []
    voltas=[]
    for linha in range(len(matriz)):
         list.append(menorestempos, min(matriz[linha]))
        for coluna in range(len(matriz)):
    return (list.index(min(menorestempos)+1), min(menorestempos))