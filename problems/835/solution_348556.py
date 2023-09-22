#Entrada: Uma matriz com 6 linhas e 10 colunas
#1)Precisamos encontrar qual o menor tempo
#2)Depois disso, encontraremos em qual volta foi e qual foi o corredor
#3)Ao final, retornaremos uma lista contendo essas informações
def melhor_volta(matriz:list)->tuple:
    """A função recebe uma matriz com dados de corredores
    ela retorna qual corredor fez uma volta mais rapido,
    em qual tempo e qual foi a volta""" 
    i=0
    menor=0
    listaAux=[]
    indice=0
    corredor=0
    for corredores in matriz:
        listaAux.append(min(corredores))
    menor=min(listaAux)
    while i < len(matriz):
        if menor in matriz[i]:
            indice=list.index(matriz[i],menor)
            corredor=i
        i+=1
    return (corredor+1,menor, indice+1)