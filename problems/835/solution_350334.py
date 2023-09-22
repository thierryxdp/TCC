def melhor_volta(matriz):
    '''khgjhg'''
    lista_menores_tempos=[]
    for linha in matriz:
        lista_menores_tempos.append(min(linha))
    melhor_volta= min(lista_menores_tempos)
    num_corredor=(lista_menores_tempos.index(melhor_volta))+1
    num_volta= (list.index(matriz[num_corredor-1],melhor_volta))+1
    return num_corredor,melhor_volta,num_volta