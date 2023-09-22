def pontos_por_time(lista):
    if lista[0][2][0]> lista[0][2][1]:
        pontosA+=3
    elif lista[0][2][0]== lista[0][2][1]:
      	pontosA+=1
        pontosB+=1
    else:
        pontosB+=3
    if lista[1][2][0]> lista[1][2][1]:
        pontosA+=3
    elif lista[1][2][0]== lista[1][2][1]:
      	pontosA+=1
        pontosB+=1
    else:
        pontosB+=3
    dici={lista[0][0]:pontosA,lista[1][0]