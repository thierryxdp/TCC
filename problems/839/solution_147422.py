def carros(p,c=5):
    if p%c>0:
        carros=(p//c)+1   
    else:
        carros=(p//c)