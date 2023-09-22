def colchao(medidas):
    if (
        medidas[0][0] <= medidas[1]
        and medidas[1] <= medidas[2]
        or medidas[0][0] <= medidas[1]
        and medidas[0][2] <= medidas[2]
        or medidas[0][1] <= medidas[1]
        and medidas[0][2] <= medidas[2]
        or medidas[0][2] <= medidas[1]
        and medidas[0][1] <= medidas[2]
        or medidas[0][0] <= medidas[2]
        and medidas[0][1] <= medidas[1]
        or medidas[0][0] <= medidas[2]
        and medidas[0][2] <= medidas[1]
    ):
        return True
    else:
        return False

print(colchao([[25,120,220],200,100]))