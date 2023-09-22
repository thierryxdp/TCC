def melhor_volta(matriz):
    '''funcao recebe uma matriz com o tempo de cada corredor e volta e retorna o corredor que fez o menor tempo na menor volta
    int-> int, int, int'''
    corredor = 0
    menor = matriz[0][0]
    
    for i in matriz:
        a = min(i)
        if a < menor:
            menor = a
    for i in matriz:
        corredor +=1
        if menor in i:
            volta = i.index(menor)
            return((corredor,menor, volta+1))