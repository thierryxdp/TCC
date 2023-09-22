def melhor_volta(matriz):
    """Função que calcula a media de uma matriz dada de entrada e retornar o seu valor arrednondado de duas acasas decimais
    list -> float"""
    total1=0
    total2=0
    total3=0
    total4=0
    total5=0
    total6=0
    listatempo=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if 0 == i:
                total1=total1+matriz[i][j]
            	list.append(listatempo,total1)
            elif 1 == i:
                total2=total2+matriz[i][j]
            	list.append(listatempo,total2)
            elif 2 == i:
                total3=total3+matriz[i][j]
            	list.append(listatempo,total3)
            elif 3 == i:
                total4=total4+matriz[i][j]
            	list.append(listatempo,total4)
            elif 4 == i:
                total5=total5+matriz[i][j]
            	list.append(listatempo,total5)
            elif 5 ===i:
                total6=total6+matriz[i][j]
            	list.append(listatempo,total6)
    return listatempo