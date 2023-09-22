def lingua_p(x):
    x=str.lower(x)
    z=0
    while z<len(x):
        if x[z]=="a":
            x=x[:z]+"ap"+x[z:]
            z=z+3
        elif x[z]=="e":
            x=x[:z]+"pe"+x[z:]
            z=z+3
        elif x[z]=="i":
            x=x[:z]+"pi"+x[z:]
            z=z+3
        elif x[z]=="o":
            x=x[:z]+"po"+x[z:]
            z=z+3
        elif x[z]=="u":
            x=x[:z]+"pu"+x[z:]
            z=z+3
        else:
            z=z+1
    return x