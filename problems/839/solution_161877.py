def carros(x,y=5):
    a=x%y
    if a==0:
        return x/y
    else:
        return int(x/y)+1