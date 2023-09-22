def melhor_volta(x):
    soma = 0
    volta1=x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],x[0][5]
    volta2=x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],x[1][5]
    volta3=x[2][0],x[2][1],x[2][2],x[2][3],x[2][4],x[2][5]
    volta4=x[3][0],x[3][1],x[3][2],x[3][3],x[3][4],x[3][5]
    volta5=x[4][0],x[4][1],x[4][2],x[4][3],x[4][4],x[4][4]
    volta6=x[5][0],x[5][1],x[5][2],x[5][3],x[5][4],x[5][5]
    volta7=x[6][0],x[6][1],x[6][2],x[6][3],x[6][4],x[6][5]
    volta8=x[7][0],x[7][1],x[7][2],x[7][3],x[7][4],x[7][5]
    volta9=x[8][0],x[8][1],x[8][2],x[8][3],x[8][4],x[8][5]
    volta10=x[9][0],x[9][1],x[9][2],x[9][3],x[9][4],x[9][5]
    return min(min(volta1),min(volta2),min(volta3),min(volta4),
    min(volta5)min(volta6)min(volta7)min(volta8)min(volta9),
    min(volta10))