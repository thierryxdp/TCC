def colchao(medidas,H,L):#verifica se um colchão passa por uma porta. list,int,int->Boolean
    Ph=H
    Pl=L
    x=medidas[0]
    y=medidas[1]
    z=medidas[2]
    if y<Ph and z>Pl or y==Ph and z>Pl:
        return True
    else:
        return False