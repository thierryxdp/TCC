def pontos_por_time(lista):
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return {str(lista[0][0]):6,str(lista[0][1]):0}
    elif lista[0][2][0]>lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return {str(lista[0][0]):3,str(lista[0][1]):3}
    elif lista[0][2][0]>lista[0][2][1] and lista[1][2][0]=lista[1][2][1]:
        return {str(lista[0][0]):4,str(lista[0][1]):1}
    elif lista[0][2][0]=lista[0][2][1] and lista[1][2][0]=lista[1][2][1]:
        return {str(lista[0][0]):2,str(lista[0][1]):2}
    elif lista[0][2][0]=lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return {str(lista[0][0]):1,str(lista[0][1]):4}
    elif lista[0][2][0]<lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return {str(lista[0][0]):0,str(lista[0][1]):6}