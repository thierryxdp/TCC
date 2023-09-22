def colchao(medidas,h,l):
    if (((medidas[0])*(medidas[1]))>(h*l)) or ((medidas[0]>h)and(medidas[0]>l)) or ((medidas[1]>h)and(medidas[1]>l)):
        a=(0==1)
    elif ((medidas[0])*(medidas[1]))<=(h*l):
        a=(0==0)
    return a