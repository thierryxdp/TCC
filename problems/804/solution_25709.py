"""função que recebe uma tupla de 4 elementos e retorna uma nova tupla apenas com os números pares.
    tupla->tupla"""
    a,b,c,d=tupla
    restoa = a%2
    restob = b%2
    restoc = c%2
    restod = d%2
    if (restoa==0) and (restob==0) and (restoc==0) and (restod==0):
        return (a,b,c,d)
    elif (restoa!=0) and (restob==0) and (restoc==0) and (restod==0):
        return (b,c,d)
    elif (restoa==0) and (restob!=0) and (restoc==0) and (restod==0):
        return (a,c,d)
    elif (restoa==0) and (restob==0) and (restoc!=0) and (restod==0):
        return (a,b,d)
    elif (restoa==0) and (restob==0) and (restoc==0) and (restod!=0):
        return (a,b,c)
    elif (restoa!=0) and (restob!=0) and (restoc==0) and (restod==0):
        return (c,d)
    elif (restoa!=0) and (restob==0) and (restoc!=0) and (restod==0):
        return (b,d)
    elif (restoa!=0) and (restob==0) and (restoc==0) and (restod!=0):
        return (b,c)
    elif (restoa==0) and (restob!=0) and (restoc==0) and (restod!=0):
        return (a,c)
    elif (restoa==0) and (restob==0) and (restoc!=0) and (restod!=0):
        return (a,b)
    elif (restoa==0) and (restob!=0) and (restoc!=0) and (restod==0):
        return (a,d)
    elif (restoa==0) and (restob!=0) and (restoc!=0) and (restod!=0):
        return (a,)
    elif (restoa!=0) and (restob==0) and (restoc!=0) and (restod!=0):
        return (b,)
    elif (restoa!=0) and (restob!=0) and (restoc==0) and (restod!=0):
        return (c,)
    elif (restoa!=0) and (restob!=0) and (restoc!=0) and (restod==0):
        return (d,)
    else:
        return '()'#Start your python function here