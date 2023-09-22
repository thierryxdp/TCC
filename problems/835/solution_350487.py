def melhor_volta(matriz):
    '''Função que retorna o menor tempo de uma
    volta dada por um corredor e de quem foi o
    feito; recebe como parâmetro uma matriz de dimensão
    6x10; list(list)-->tuple'''
    lista_menor_tempo=[]
    lista_volta=[]
    for linha in range(len(matriz)):
        list.append(lista_menor_tempo,min(matriz[linha]))
        posv=list.index(matriz[linha],min(matriz[linha]))
        list.append(lista_volta,posv)
    menor=min(lista_menor_tempo)
    pos=list.index(lista_menor_tempo,min(lista_menor_tempo))
    return pos+1,menor,lista_volta[pos]+1