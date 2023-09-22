def repetidos(x):
    resposta=0
    t=0
    while t<(len(x)-1):
        if x[t]==x[t+1]:
            resposta+=1
        t+=1
    return resposta