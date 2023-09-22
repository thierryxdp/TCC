def lingua_p(x):
    x=str.lower(x)
    z=0
    while z<len(x):
        if x(z)==a:
            x=x[:z]+"p"+x[z:]
            z=z+1
        elif x(z)=="e":
            x=x[:z]+"p"+x[z:]
            z=z+1
        elif x(z)=="i":
            x=x[:z]+"p"+x[z:]
            z=z+1
        elif x(z)=="o":
            x=x[:z]+"p"+x[z:]
            z=z+1
        elif x(z)=="u":
            x=x[:z]+"p"+x[z:]
            z=z+1
        else:
            z=z+1
        return x